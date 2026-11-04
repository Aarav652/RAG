import os
import subprocess
files=os.listdir("videos")

for file in files:
    file_name=file.split('#')[0]
    tutorial_no=file.split('.')[0].split('#')[1]
    print(f"File Name: {file_name}, Tutorial No: {tutorial_no}")
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"mp3/{tutorial_no} {file_name}.mp3"])

import os
import subprocess


subprocess.run(["ffmpeg", "-i", "mp3/2 first html .mp3", "-t", "10", "-c", "copy", "sample.mp3"])
