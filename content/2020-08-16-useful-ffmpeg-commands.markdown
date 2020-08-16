---
layout: post
title: Useful FFmpeg commands for video editing
date: Sun 16 Aug 14:33:32 CEST 2020
comments: true
slug: useful-ffmpeg-commands
tags: FFmpeg
---

As a response to Antonio Terceiro’s [blog post](https://terceiro.xyz/2020/08/15/useful-ffmpeg-commands-for-editing-video/), I’m publishing some FFmpeg commands I’ve been using recently.

#### Embedding subtitles

Sometimes you have a video with subtitles in multiple languages and you don’t want to clutter the directory with a lot of similarly-named files — or maybe you want to be able to easily transfer the video and subtitles at once. In this case, it may be useful to embed to subtitles directly into the video container file.

    ffmpeg -i video.mp4 -i video.eng.srt -map 0:v -map 0:a -c copy -map 1 \
            -c:s:0 mov_text -metadata:s:s:0 language="eng" video-out.mp4

This commands recodes the subtitle file into a format appropriate for the MP4 container and embeds it with a metadata element telling the video player what language it is in. You can add multiple subtitles at once, or you can also transcode the audio to AAC while doing so (I found that a lot of Android devices can’t play Ogg Vorbis streams):

    ffmpeg -i video.mp4 -i video.deu.srt -i video.eng.srt -map 0:v -map 0:a \
            -c:v copy -c:a aac -map 1 -c:s:0 mov_text -metadata:s:s:0 language="deu" \
                               -map 2 -c:s:1 mov_text -metadata:s:s:1 language="eng" video-out.mp4

#### ‘Hard’ subtitles

Sometimes you need to play the video with subtitles on devices not supporting them. In that case, it may be useful to ‘hardcode’ the subtitles directly into the video stream:

    ffmpeg -i video.mp4 -vf subtitles=video.eng.srt video-out.mp4

Unfortunately, if you also want to apply more transformations to the video, it starts getting tricky, the `-vf` option is no longer enough:

    ffmpeg -i video.mp4 -i overlay.jpg -filter:a "volume=10" \
            -filter_complex '[0:v][1:v]overlay[outv];[outv]subtitles=video.eng.srt' \
                            video-out.mp4

This command adds an overlay to the video stream (in my case I overlaid a full frame over the original video offering some explanations), increases the volume ten times and adds hard subtitles.

P.S. You can see the practical application of the above in this [video with a head of one of the electoral commissions in Belarus forcing the members of the staff to manipulate the voting results](https://www.youtube.com/watch?v=i_PEv2SO2yU). I transcribed the video in both Russian and English and encoded the English subtitles into the video.
