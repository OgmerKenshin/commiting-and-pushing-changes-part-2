#It's literally 4am and I just figured out how to download ffmpeg
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment
def download_youtube_audio(youtube_url, output_dir="downloads"):
    """
    Downloads the audio from the YouTube video at the specified URL and converts it to MP3 format.
    """
   #1st commit without changes
   