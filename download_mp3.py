"""
download_mp3.py

Downloads the audio track of a single YouTube video and saves it
as an MP3 file using pytube.

Usage:
    python download_mp3.py <YOUTUBE_VIDEO_URL> [<OUTPUT_PATH>]
"""

import sys
import os
from pytube import YouTube

def download_youtube_mp3(url, output_path="./"):
    try:
        yt = YouTube(url)
        
        # Get the audio-only stream (e.g., webm format)
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        print(f"Downloading audio from: {yt.title}")
        out_file = audio_stream.download(output_path=output_path)
        
        # Convert the downloaded file to .mp3
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        
        # Rename the file
        os.rename(out_file, new_file)
        
        print(f"MP3 download completed: {new_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_mp3.py <YOUTUBE_VIDEO_URL> [<OUTPUT_PATH>]")
        sys.exit(1)

    video_url = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "./"
    
    download_youtube_mp3(video_url, output_folder)
