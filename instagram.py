from instagrapi import Client
import os

exportRoot =  os.getcwd() + "\\images\\"
exportRoot.replace('\\', '/')
 
def upload(n):
    cl = Client()
    cl.login("missed_connections_bot", "long ass password")

    album_path = []
    
    for i in range(n):
        path = exportRoot + str(i) + ".jpg"
        
        album_path.append(path)

        if len(album_path) == 10 or i+1 == n:
            if len(album_path) == 1:
                cl.photo_upload(album_path, caption="")
                print("Photo uploaded")
            else:
                cl.album_upload(album_path, caption="")
                print("Album uploaded")
                album_path = []
        
    dir = exportRoot
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))