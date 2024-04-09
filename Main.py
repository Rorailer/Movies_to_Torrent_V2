#!/moviesapi/bin/python

from modules import *
import time


running = True
while running == True:
    print('''What Would You Like to Do?
    1. Search for Movie
    2. Quit''')

    user = input('==> ')

    clear()

    if user == '1':
        query = input('Enter Movie Name: ')
        movies = search(query)
        if movies != None:
            
            for i, movie in enumerate(movies):
                movie['index'] = i+1
                print(f"{i+1}. {movie['title']} ({movie['year']})")

            user = input('Enter Index of Movie to Download: ')
            
            torrent_link = movies[int(user)-1]['torrents']
            torrent_link = [d for d in torrent_link if d['quality'] == '1080p']
            
            name = movies[int(user)-1]['title_english']
            name = name.replace(' ','_')
            
            path = download(torrent_link[0]['url'],name)

            add_torrent(path)
            clear()
            print("Download Started")
            time.sleep(1)
            del_trash(path)
            clear()
        
        
        
        
        else:
            print("No Movies Found")
            input('Press Enter to Continue')
            
    elif user == '2':
        running = False
        