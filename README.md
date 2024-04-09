# Movies_to_Torrent_V2
A simple program that searches for movies using YTS API , downloads its .torrent file and then automatically starts to download it using qbittorrent web ui.

# Replace user and password
In Modules.py replace 'user' and 'password' with the username and password of your qbittorrent webui.

---
# rename.py
---
rename.py is an additional file that you may or may not need. This file cleans up the name of the folder and files within that folder and moves it to your desired location. For example: '300 Rise of an Empire (2014) [1080p]' This turns into '300 Rise of an Empire (2014)' and '300.Rise.of.an.Empire.2014.1080p.BluRay.x264.YIFY.mp4' This turns into '300 Rise of an Empire.mp4'

This file is useful if you are using a media server which requires naming to be pretty precise.
