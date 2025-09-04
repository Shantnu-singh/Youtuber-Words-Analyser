from pytube import Playlist 
TrfProd = "https://www.youtube.com/playlist?list=PLaGGM00HkKkvDwVXbPG8ZVLyQ3SlKahPK"
Playlist._video_regex = r"\"url\":\"(/watch\?v=[\w-]*)"
playlist = Playlist(TrfProd)
playlist.title , playlist.length , playlist.owner , playlist.playlist_url , playlist.video_urls
print(playlist.video_urls)