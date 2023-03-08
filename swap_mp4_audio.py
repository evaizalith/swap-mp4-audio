from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from os import path, walk
import sys

video_folder = sys.argv[1]
audio_folder = sys.argv[2]
output_folder = sys.argv[3]

if not path.exists(video_folder):
    print("Error: no video folder")
    exit()
if not path.exists(audio_folder):
    print("Error: no audio folder")
    exit()
if not path.exists(output_folder):
    output_folder = getcwd()

count = 0
video_paths = []
video_files = []
for (root, dirnames, filenames) in walk(video_folder):
    video_paths.append(root)

    for name in filenames:
        video_files.append(name)

audio_paths = []
audio_files = []
for (root, dirnames, filenames) in walk(audio_folder):
    audio_paths.append(root)

    for name in filenames:
        audio_files.append(name)

n_items = len(video_files)
for i in range(n_items):
    video = VideoFileClip(video_paths[i] + video_files[i])
    audio = AudioFileClip(audio_paths[i] + audio_files[i])

    video = video.set_audio(audio)

    video.write_videofile(output_folder + video_files[i])

print(f"Combined {n_items} clips.")