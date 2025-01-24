"""
download_playlist_mp3.py

Downloads the audio track of all videos in a YouTube playlist
and saves each one as an MP3 file using pytube and pydub.

Usage:
    python download_playlist_mp3.py <PLAYLIST_URL> [<OUTPUT_PATH>]
"""
### yt-dlp --yes-playlist --extract-audio --audio-format mp3 --output "./mp3_downloads/%(playlist_index)s - %(title)s.%(ext)s" "https://youtube.com/playlist?list=PL38D77677DCAEABD5&si=cu004y8kMCw7Md2J"

import os
import sys
from pytube import Playlist, YouTube
from pydub import AudioSegment

def download_playlist_as_mp3(playlist_url, output_path="./mp3_downloads"):
    try:
        pl = Playlist(playlist_url)
        print(f"Playlist title: {pl.title}")
        print(f"Number of videos: {len(pl.video_urls)}")

        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        for url in pl.video_urls:
            try:
                yt = YouTube(url)
                audio_stream = yt.streams.filter(only_audio=True).first()
                print(f"Downloading audio from: {yt.title}")

                # Download the audio file
                out_file = audio_stream.download(output_path=output_path)

                # Convert to MP3 using pydub
                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"
                AudioSegment.from_file(out_file).export(new_file, format="mp3")

                # Remove the original file
                os.remove(out_file)

                print(f"Saved MP3: {new_file}\n")

            except Exception as e:
                print(f"Could not download {url}: {e}")

        print("All playlist items downloaded as MP3!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_playlist_mp3.py <PLAYLIST_URL> [<OUTPUT_PATH>]")
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "./mp3_downloads"

    download_playlist_as_mp3(playlist_url, output_folder)
