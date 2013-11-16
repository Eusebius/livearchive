#!/usr/bin/python

# v0.91 : part files are not managed, only fully downloaded files


import os, random, time

dirName = "archived"
suffixChars = "abcdefghijklmnopqrstuvwxyz"

if not os.path.exists(dirName):
    os.makedirs(dirName)
else:
    if not os.path.isdir(dirName):
        print dirName + " exists and is not a directory. Exiting."

while(True):
    for file in os.listdir("."):
        if ((os.path.isfile(file)) and (file[-5:] != '.part') and (file[-4:] != '.flv') and not (os.path.isfile(file + '.part'))):
            newFile = dirName + "/" + file
            while (os.path.exists(newFile)):
                [base, ext] = os.path.splitext(newFile)
                base += ''.join(random.choice(suffixChars) for x in range(3))
                newFile = base + ext
            os.rename(file, newFile)
    time.sleep(30)
