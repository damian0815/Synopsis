//
//  FrameCounterPlugin.h
//  MetadataTranscoderTestHarness
//
//  Created by vade on 4/3/15.
//  Copyright (c) 2015 Synopsis. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreMedia/CoreMedia.h>
#import "AnalyzerPluginProtocol.h"

@interface FrameCounterPlugin : NSObject <AnalyzerPluginProtocol>

@property (readonly) NSString* pluginName;
@property (readonly) NSString* pluginIdentifier;

@property (readonly) NSArray* pluginAuthors;

@property (readonly) NSString* pluginDescription;

@property (readonly) NSUInteger pluginAPIVersionMajor;
@property (readonly) NSUInteger pluginAPIVersionMinor;

@property (readonly) NSUInteger pluginVersionMajor;
@property (readonly) NSUInteger pluginVersionMinor;

@property (readonly) NSDictionary* pluginReturnedMetadataKeysAndDataTypes;

@property (readonly) NSString* pluginMediaType;

@property (readonly) BOOL hasModules;

- (void) beginMetadataAnalysisSessionWithQuality:(SynopsisAnalysisQualityHint)qualityHint forModule:(NSString*)moduleName;

- (NSDictionary*) analyzedMetadataDictionaryForVideoBuffer:(void*)baseAddress width:(size_t)width height:(size_t)height bytesPerRow:(size_t)bytesPerRow forModule:(NSString*)moduleName error:(NSError**)error;

- (NSDictionary*) finalizeMetadataAnalysisSessionWithError:(NSError**)error;

@end
