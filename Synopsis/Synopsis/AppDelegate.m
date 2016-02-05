//
//  AppDelegate.m
//  MetadataTranscoderTestHarness
//
//  Created by vade on 3/31/15.
//  Copyright (c) 2015 Synopsis. All rights reserved.
//

#import "AppDelegate.h"

#import "DropFilesView.h"
#import "LogController.h"
#import "AnalyzerPluginProtocol.h"

#import "AnalysisAndTranscodeOperation.h"
#import "MetadataWriterTranscodeOperation.h"

#import "PreferencesViewController.h"
#import "PresetObject.h"

@interface AppDelegate ()

@property (weak) IBOutlet NSWindow *window;
@property (weak) IBOutlet DropFilesView* dropFilesView;

@property (atomic, readwrite, strong) NSOperationQueue* transcodeQueue;
@property (atomic, readwrite, strong) NSOperationQueue* metadataQueue;

@property (atomic, readwrite, strong) NSMutableArray* analyzerPlugins;
@property (atomic, readwrite, strong) NSMutableArray* analyzerPluginsInitializedForPrefs;

// Preferences
@property (weak) IBOutlet NSWindow* prefsWindow;
@property (weak) IBOutlet PreferencesViewController* prefsViewController;
@property (weak) IBOutlet NSArrayController* prefsAnalyzerArrayController;
// Log
@property (weak) IBOutlet NSWindow* logWindow;

// Toolbar
@property (weak) IBOutlet NSToolbarItem* startPauseToolbarItem;



@end

@implementation AppDelegate


//fix our giant memory leak which happened because we are probably holding on to Operations unecessarily now and not letting them go in our TableView's array of cached objects or some shit.


- (id) init
{
    self = [super init];
    if(self)
    {
        // Serial transcode queue
        self.transcodeQueue = [[NSOperationQueue alloc] init];
        self.transcodeQueue.maxConcurrentOperationCount = NSOperationQueueDefaultMaxConcurrentOperationCount; //1, NSOperationQueueDefaultMaxConcurrentOperationCount
        
        // Serial metadata / passthrough writing queue
        self.metadataQueue = [[NSOperationQueue alloc] init];
        self.metadataQueue.maxConcurrentOperationCount = NSOperationQueueDefaultMaxConcurrentOperationCount; //1, NSOperationQueueDefaultMaxConcurrentOperationCount
        
        self.analyzerPlugins = [NSMutableArray new];
        self.analyzerPluginsInitializedForPrefs = [NSMutableArray new];
    }
    return self;
}

- (void) awakeFromNib
{
    self.dropFilesView.dragDelegate = self;
    
    self.prefsAnalyzerArrayController.content = self.analyzerPluginsInitializedForPrefs;
}

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    
    // REVEAL THYSELF
    [[self window] makeKeyAndOrderFront:nil];
    
    // Touch a ".synopsis" file to trick out embedded spotlight importer that there is a .synopsis file
    // We mirror OpenMeta's approach to allowing generic spotlight support via xattr's
    // But Yea
    [self initSpotlight];
    
    // Load our plugins
    NSString* pluginsPath = [[NSBundle mainBundle] builtInPlugInsPath];
    
    NSError* error = nil;
    
    NSArray* possiblePlugins = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:pluginsPath error:&error];
    
    if(!error)
    {
        for(NSString* possiblePlugin in possiblePlugins)
        {
            NSBundle* pluginBundle = [NSBundle bundleWithPath:possiblePlugin];
            
            NSError* loadError = nil;
            if([pluginBundle preflightAndReturnError:&loadError])
            {
                if([pluginBundle loadAndReturnError:&loadError])
                {
                    // Weve sucessfully loaded our bundle, time to cache our class name so we can initialize a plugin per operation
                    // See (AnalysisAndTranscodeOperation
                    Class pluginClass = pluginBundle.principalClass;
                    NSString* classString = NSStringFromClass(pluginClass);
                    
                    if(classString)
                    {
                        [self.analyzerPlugins addObject:classString];
                        
                        [[LogController sharedLogController] appendSuccessLog:[NSString stringWithFormat:@"Loaded Plugin: %@", classString, nil]];
                        
                        [self.prefsAnalyzerArrayController addObject:[[pluginClass alloc] init]];
                        
                    }
                }
                else
                {
                    [[LogController sharedLogController] appendErrorLog:[NSString stringWithFormat:@"Error Loading Plugin : %@ : %@", [pluginsPath lastPathComponent], loadError, nil]];
                }
            }
            else
            {
                [[LogController sharedLogController] appendErrorLog:[NSString stringWithFormat:@"Error Preflighting Plugin : %@ : %@", [pluginsPath lastPathComponent], loadError, nil]];
            }
        }
    }
    
//    [self initPrefs];
}

#pragma mark - Prefs

- (void) initSpotlight
{
    NSURL* spotlightFileURL = nil;
    NSURL* resourceURL = [[NSBundle mainBundle] resourceURL];
    
    spotlightFileURL = [resourceURL URLByAppendingPathComponent:@"spotlight.synopsis"];
    
    if([[NSFileManager defaultManager] fileExistsAtPath:[spotlightFileURL path]])
    {
        [[NSFileManager defaultManager] removeItemAtPath:[spotlightFileURL path] error:nil];
        
//        // touch the file, just to make sure
//        NSError* error = nil;
//        if(![[NSFileManager defaultManager] setAttributes:@{NSFileModificationDate:[NSDate date]} ofItemAtPath:[spotlightFileURL path] error:&error])
//        {
//            NSLog(@"Error Initting Spotlight : %@", error);
//        }
    }
    
    {
        // See OpenMeta for details
        // Our spotlight trickery file will contain a set of keys we use

        // info_v002_synopsis_dominant_color_values = rgba
        NSDictionary* exampleValues = @{ @"info_v002_synopsis_dominant_color_values" : @[@0.0, @0.0, @0.0, @1.0], // Solid Black
                                         @"info_v002_synopsis_dominant_color_name" : @"Black",
                                         
                                         @"info_v002_synopsis_motion_vector_name" : @"Left",
                                         @"info_v002_synopsis_motion_vector_values" : @[@-1.0, @0.0]
                                        };
        
        [exampleValues writeToFile:[spotlightFileURL path] atomically:YES];
    }
}

#pragma mark -

- (IBAction)openMovies:(id)sender
{
    // Open a movie or two
    NSOpenPanel* openPanel = [NSOpenPanel openPanel];
    
    [openPanel setAllowsMultipleSelection:YES];
    
    // TODO
    [openPanel setAllowedFileTypes:[AVMovie movieTypes]];
    //    [openPanel setAllowedFileTypes:@[@"mov", @"mp4", @"m4v"]];
    
    [openPanel beginSheetModalForWindow:[self window] completionHandler:^(NSInteger result)
     {
         if (result == NSFileHandlingPanelOKButton)
         {
             for(NSURL* fileurl in openPanel.URLs)
             {
                 [self enqueueFileForTranscode:fileurl];
             }
         }
     }];
}
- (void) enqueueFileForTranscode:(NSURL*)fileURL
{
    NSString* lastPath = [fileURL lastPathComponent];
    NSString* lastPathExtention = [fileURL pathExtension];
    lastPath = [lastPath stringByAppendingString:@"_transcoded"];
    NSString* lastPath2 = [lastPath stringByAppendingString:@"_analyzed"];
    
    NSURL* destinationURL = [fileURL URLByDeletingLastPathComponent];
    destinationURL = [destinationURL URLByDeletingPathExtension];
    destinationURL = [[destinationURL URLByAppendingPathComponent:lastPath] URLByAppendingPathExtension:lastPathExtention];
    
    NSURL* destinationURL2 = [fileURL URLByDeletingLastPathComponent];
    destinationURL2 = [destinationURL2 URLByDeletingPathExtension];
    destinationURL2 = [[destinationURL2 URLByAppendingPathComponent:lastPath2] URLByAppendingPathExtension:lastPathExtention];
    
    // Pass 1 is our analysis pass, and our decode pass

    // todo: get the selected preset and fill in the logic here
    PresetObject* currentPreset = [self.prefsViewController defaultPreset];
    PresetVideoSettings* videoSettings = currentPreset.videoSettings;
    PresetAudioSettings* audioSettings = currentPreset.audioSettings;
    
    NSDictionary* transcodeOptions = @{kSynopsisTranscodeVideoSettingsKey : (videoSettings.settingsDictionary) ? videoSettings.settingsDictionary : [NSNull null],
                                       kSynopsisTranscodeAudioSettingsKey : (audioSettings.settingsDictionary) ? audioSettings.settingsDictionary : [NSNull null],
                                       };
    
    // TODO: Just pass a copy of the current Preset directly.
    AnalysisAndTranscodeOperation* analysis = [[AnalysisAndTranscodeOperation alloc] initWithSourceURL:fileURL
                                                                                        destinationURL:destinationURL
                                                                                      transcodeOptions:transcodeOptions
                                                                                    availableAnalyzers:self.analyzerPlugins];
    
    assert(analysis);
    
    // pass2 is depended on pass one being complete, and on pass1's analyzed metadata
    __weak AnalysisAndTranscodeOperation* weakAnalysis = analysis;
    
    analysis.completionBlock = (^(void)
                                {
                                    // Retarded weak/strong pattern so we avoid retain loopl
                                    __strong AnalysisAndTranscodeOperation* strongAnalysis = weakAnalysis;
                                    
                                    NSDictionary* metadataOptions = @{kSynopsisAnalyzedVideoSampleBufferMetadataKey : strongAnalysis.analyzedVideoSampleBufferMetadata,
                                                                      kSynopsisAnalyzedAudioSampleBufferMetadataKey : strongAnalysis.analyzedAudioSampleBufferMetadata,
                                                                      kSynopsisAnalyzedGlobalMetadataKey : strongAnalysis.analyzedGlobalMetadata
                                                                      };
                                    
                                    MetadataWriterTranscodeOperation* pass2 = [[MetadataWriterTranscodeOperation alloc] initWithSourceURL:destinationURL destinationURL:destinationURL2 metadataOptions:metadataOptions];
                                    
                                    pass2.completionBlock = (^(void)
                                                             {
                                                                 [[LogController sharedLogController] appendSuccessLog:@"Finished Transcode and Analysis"];
                                                             });
                                    
                                    dispatch_async(dispatch_get_main_queue(), ^{
                                        [[NSNotificationCenter defaultCenter]  postNotificationName:kSynopsisNewTranscodeOperationAvailable object:pass2];
                                    });
                                    
                                    [self.metadataQueue addOperation:pass2];
                                    
                                });
    
    [[LogController sharedLogController] appendVerboseLog:@"Begin Transcode and Analysis"];
    
    dispatch_async(dispatch_get_main_queue(), ^{
        [[NSNotificationCenter defaultCenter]  postNotificationName:kSynopsisNewTranscodeOperationAvailable object:analysis];
    });
    
    
    [self.transcodeQueue addOperation:analysis];
}


- (void)applicationWillTerminate:(NSNotification *)aNotification {
    // Insert code here to tear down your application
}

#pragma mark - Drop File Helper

- (void) handleDropedFiles:(NSArray *)fileURLArray
{
    for(NSURL* url in fileURLArray)
    {
        [self enqueueFileForTranscode:url];
    }
}

#pragma mark - Toolbar

static BOOL isRunning = NO;
- (IBAction) runAnalysisAndTranscode:(id)sender
{
    isRunning = !isRunning;
    
    if(isRunning)
    {
        self.startPauseToolbarItem.image = [NSImage imageNamed:@"ic_pause_circle_filled"];
    }
    else
    {
        self.startPauseToolbarItem.image = [NSImage imageNamed:@"ic_play_circle_filled"];
    }
}

- (IBAction) revealLog:(id)sender
{
    [self revealHelper:self.logWindow sender:sender];
}

- (IBAction) revealPreferences:(id)sender
{
    [self revealHelper:self.prefsWindow sender:sender];
}

#pragma mark - Helpers

- (void) revealHelper:(NSWindow*)window sender:(id)sender
{
    if([window isVisible])
    {
        [window orderOut:sender];
    }
    else
    {
        [window makeKeyAndOrderFront:sender];
    }
}

@end
