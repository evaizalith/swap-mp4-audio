# swap-mp4-audio

This script takes in three inputs:
  - a folder full of .mp4 files (video)
  - another folder of .mp4 or .mp3 files (audio)
  - an output folder

The script will iterate through the list of videos, pair them with an audio file that has the same index, and set the audio component of the video to equal the audio file passed to it. 

This is intended to be used to make it easier to download videos from online video hosting websites. Some of them have an API that lets you download the video, but they split it up into its video and audio components. Manually stitching them together is tedious, so I made this script to do it for me. 
