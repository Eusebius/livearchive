 
#!/usr/bin/python

# v1.0


import os, random, time, hashlib

dirName = "archived"
hDirName = "hash"
suffixChars = "abcdefghijklmnopqrstuvwxyz"
chunksize = 16*1024*1024

if not os.path.exists(dirName):
    os.makedirs(dirName)
else:
    if not os.path.isdir(dirName):
        print dirName + " exists and is not a directory. Exiting."
if not os.path.exists(hDirName):
    os.makedirs(hDirName)
else:
    if not os.path.isdir(hDirName):
        print hDirName + " exists and is not a directory. Exiting."

while(True):
    for file in os.listdir("."):
        if (os.path.isfile(file) and (not os.path.exists(file + '.part')) and (not file[-5:] == ".part")):
            hasher = hashlib.md5()
            f = open(file, "rb")
            buf = f.read(chunksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(chunksize)
            f.close()
            hName = hasher.hexdigest()
            hFileName = hDirName + "/" + hName + ".txt"
            #data = data.encode('hex')
            if (os.path.exists(hFileName)):
                try:
                    print "*** Already encountered: " + file[:50]
                    os.remove(file)
                except:
                    pass
            else:
                newFile = dirName + "/" + file
                while (os.path.exists(newFile)):
                    [base, ext] = os.path.splitext(newFile)
                    base += ''.join(random.choice(suffixChars) for x in range(3))
                    newFile = base + ext
                try:
                    os.rename(file, newFile)
                    os.utime(newFile, None)
                    hf = open(hFileName, 'w').close()
                    print "     ++ " + file[:50]
                except OSError as e:
                    pass
                    #print "     -- OSError: " + file[:50]
                except WindowsError as e:
                    pass
                    #print "     -- WindowsError: " + file[:50]
    time.sleep(30)
