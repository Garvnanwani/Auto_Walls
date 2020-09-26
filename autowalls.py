import requests
import wget
import ctypes
import time


def getWall():
    access_key = "" #Put your unsplash API access_key here
    url = "https://api.unsplash.com/photos/random/?client_id=" + access_key
    params = {
        "query": "HD Wallpapers",  #you can set any query you want
        "orientation": "landscape", #landscape photos will be best suited for wallpapers
    }
    response = requests.get(url, params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, "C:\Windows\Temp\wallpaper.jpg")
    return wallpaper


def setWal():
    wallpaper = getWall()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)  #this function helps to change the wallpaper through windows commands, you can do similar things for mac or linux.


def run_script():
    try:
        while True:
            setWal()
            time.sleep(5)   #here you can set the time interval after which you want the wallpaper to change
    except KeyboardInterrupt:
        print("\nHope you liked the wallpaper") #Whenever you like any wallpaper, you can close the script to keep the wallpaper
    except Exception:
        pass


if __name__ == '__main__':
    run_script()
