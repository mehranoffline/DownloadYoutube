# """
# download_video.py

# Downloads a single YouTube video at the highest available resolution
# using pytube.

# Usage:
#     python download_video.py <YOUTUBE_VIDEO_URL> [<OUTPUT_PATH>]
# """

# import os
# import sys
# import pytube.request
# from pytube import YouTube

# # 1) Override the default User-Agent
# pytube.request.default_headers["User-Agent"] = (
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#     "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# )

# # 2) Adjust the default range request size (5MB in this example)
# # Sometimes 9MB (9437184) works better, or 10MB (10485760).
# pytube.request.default_range_size = 5 * 1024 * 1024

# def download_youtube_video(url, output_path="./"):
#     try:
#         # Create the YouTube object
#         yt = YouTube(url)
        
#         # Select the highest-resolution stream
#         stream = yt.streams.get_highest_resolution()
        
#         print(f"Downloading video: {yt.title}")
        
#         # Download to the specified path
#         stream.download(output_path=output_path)
        
#         print("Video download completed!")
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python download_video.py <YOUTUBE_VIDEO_URL> [<OUTPUT_PATH>]")
#         # Example: python download_video.py https://www.youtube.com/watch?v=fNk_zzaMoSs ./downloads
#         sys.exit(1)

#     video_url = sys.argv[1]
#     output_folder = sys.argv[2] if len(sys.argv) > 2 else "./"

#     download_youtube_video(video_url, output_folder)
import subprocess

def download_with_ytdlp(url, output_path="./"):
    cmd = [
        "yt-dlp",
        url,
        "-o", f"{output_path}/%(title)s.%(ext)s"
    ]
    subprocess.run(cmd, check=True)

download_with_ytdlp("https://www.youtube.com/watch?v=fNk_zzaMoSs", "./downloads")