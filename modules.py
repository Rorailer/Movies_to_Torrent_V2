import qbittorrentapi.torrents
import requests
import os
import subprocess
import qbittorrentapi


url = 'https://yts.mx/api/v2/list_movies.json'
home_dir = os.path.expanduser("~")


#QBittorrent Stuff
connection_info = dict(host='127.0.0.1',
                       port='8080',
                       username='user',
                       password='password')
qb = qbittorrentapi.Client(**connection_info, VERIFY_WEBUI_CERTIFICATE=False)










def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def search(query):
    response = requests.get(url+'?limit=50&query_term='+query)
    data = response.json()
    if response.status_code == 200:
        return data['data']['movies']
        
        




def download(link,name):
    path = os.path.join(home_dir,'Downloads/Torrents',f"{name}.torrent")
    subprocess.run(['curl','-o',path,link])
    return path
    
def add_torrent(torrent_link):
    try:
        qb.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)    
    qb.torrents_add(urls=torrent_link)
    
    qb.auth_log_out()
    
    
    
def del_trash(path):
    
    os.remove(f"{path}")
