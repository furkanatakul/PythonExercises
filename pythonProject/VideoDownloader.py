import pytube
from pytube import YouTube

pytube.YouTube("").streams.get_by_resolution("1080p").download("C:\\Users\\Furkan\\Downloads")
