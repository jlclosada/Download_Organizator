from PIL import Image
import os
import tkinter
from tkinter import filedialog


tkinter.Tk().withdraw()

downloadsFolder = filedialog.askdirectory()

list = ["Pictures", "Videos", "Docs", "Music"]


path_list = []
for element in list:
    path = downloadsFolder + "/" + element
    if os.path.exists(path):
        print(f"Folder '{element}' already exists")
        path_list.append(path)
    else:
        os.mkdir(path)
        path_list.append(path)

picturesFolder = path_list[0]
videosFolder = path_list[1]
docsFolder = path_list[2]
musicFolder = path_list[3]

if __name__ == '__main__':
    pictureList = []
    videoList = []
    docList = []
    musicList = []

    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + "/" + filename)

        #Images
        if extension in [".jpeg", ".jpg", ".png"]:
            picture = Image.open(downloadsFolder + "/" + filename)
            pictureList.append(picture)
            picture.save(picturesFolder + "/" + filename)
            os.remove(downloadsFolder + "/" + filename)
        count0 = len(pictureList)

        #Videos
        if extension in [".mp4", ".avi", ".mov"]:
            video = filename
            os.rename(downloadsFolder + "/" + filename, videosFolder + "/" + filename)
            videoList.append(video)
        count1 = len(videoList)

        #Documents
        if extension in [".pdf", ".doc", ".docx"]:
            doc = filename
            os.rename(downloadsFolder + "/" + filename, docsFolder + "/" + filename)
            docList.append(doc)
        count2 = len(docList)

        #Music
        if extension in [".mp3"]:
            music = filename
            os.rename(downloadsFolder + "/" + filename, musicFolder + "/" + filename)
            musicList.append(music)
        count3 = len(musicList)

    print(f"{count0} elements were moved to the Pictures folder")
    print(f"{count1} elements were moved to the Videos folder")
    print(f"{count2} elements were moved to the Documents folder")
    print(f"{count3} elements were moved to the Music folder")