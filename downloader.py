import yt_dlp
import os

def mp3_download(search_query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet' : True,
        'outtmpl' : 'downloads/%(title)s.%(ext)s',
        'postprocessors':[{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
        'ffmpeg_location': r'C:\\Users\\Nande\\Documents\\ffmpeg\\bin\\ffmpeg.exe',
        'ffprobe_location': r'C:\\Users\\Nande\\Documents\\ffmpeg\\bin\\ffprobe.exe',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(f"ytsearch:{search_query}", download=True)
        filename = ydl.prepare_filename(result['entries'][0])
        mp3_file = filename.replace('.webm', '.mp3').replace('.m4a' , '.mp3')