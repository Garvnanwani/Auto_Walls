import requests
import wget
import ctypes
import time


def getWall():
    access_key = "Y5MVF2GHEwKss-KIWb241FZ8EiG43j7pyLi3wTYvtYU"
    url = "https://api.unsplash.com/photos/random/?client_id=" + access_key
    params = {
        "query": "HD Wallpapers",
        "orientation": "landscape",
    }
    response = requests.get(url, params).json()
    image_url = response['urls']['full']
    wallpaper = wget.download(image_url, "C:\Windows\Temp\wallpaper.jpg")
    return wallpaper


def setWal():
    wallpaper = getWall()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 0)


def run_script():
    try:
        while True:
            setWal()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nHope you liked the wallpaper")
    except Exception:
        pass


if __name__ == '__main__':
    run_script()
