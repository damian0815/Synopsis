//
//  TranscodeOperation.h
//  MetadataTranscoderTestHarness
//
//  Created by vade on 3/31/15.
//  Copyright (c) 2015 Synopsis. All rights reserved.
//

#import "BaseTranscodeOperation.h"

@interface AnalysisAndTranscodeOperation : BaseTranscodeOperation

// NSArrays of AVTimedMetadataGroups that contain time ranges and metadata.
// For our second pass where we write out our metadata to the final file.
// Only available on completion / main being returned
@property (copy) NSMutableArray* analyzedVideoSampleBufferMetadata;
@property (copy) NSMutableArray* analyzedAudioSampleBufferMetadata;
@property (copy) NSDictionary* analyzedGlobalMetadata;

@property (assign) BOOL succeeded;

- (instancetype) initWithSourceURL:(NSURL*)sourceURL destinationURL:(NSURL*)destinationURL transcodeOptions:(NSDictionary*)transcodeOptions NS_DESIGNATED_INITIALIZER;

- (instancetype) init NS_UNAVAILABLE;



@end
