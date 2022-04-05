from instagrapi import Client
import os
 
def upload(n):
    cl = Client()
    cl.login("missed_connections_bot", "long ass password")

    album_path = []
    
    for i in range(n):
        path = "C:/Users/gabdr/Documents/Projects/MissedConn/images/" + str(i) + ".jpg"
        
        album_path.append(path)

        print("i: " + str(i) + ", n: " + str(n))
        print(path + "\n")

        if len(album_path) == 10 or i+1 == n:
            if len(album_path) == 1:
                cl.photo_upload(album_path, caption="")
            else:
                cl.album_upload(album_path, caption="")
                album_path = []
        
    dir = "C:/Users/gabdr/Documents/Projects/MissedConn/images/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))