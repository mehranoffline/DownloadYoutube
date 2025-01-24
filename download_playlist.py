"""
download_playlist.py

Downloads all videos in a YouTube playlist using pytube.

Usage:
    python download_playlist.py <PLAYLIST_URL> [<OUTPUT_PATH>]
"""

import sys
from pytube import Playlist

def download_youtube_playlist(playlist_url, output_path="./"):
    try:
        playlist = Playlist(playlist_url)
        
        print(f"Playlist title: {playlist.title}")
        print(f"Number of videos: {len(playlist.video_urls)}")
        
        for url in playlist.video_urls:
            try:
                print(f"Downloading from: {url}")
                yt = playlist.yt_class(url)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path=output_path)
                print(f"Completed: {yt.title}\n")
            except Exception as e:
                print(f"Could not download {url}: {e}")
                
        print("Playlist download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_playlist.py <PLAYLIST_URL> [<OUTPUT_PATH>]")
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else "./"

    download_youtube_playlist(playlist_url, output_folder)
