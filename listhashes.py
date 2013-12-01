 
#!/usr/bin/python

# v1.0


import os, hashlib

def processDir(dir):
    print dir
    chunksize = 16*1024*1024
    for file in os.listdir(dir):
        file = dir + "/" + file
        if os.path.isfile(file):
            try:
                #f = open(file, "rb")
                #data = f.read()
                #f.close()
                #hName = hashlib.md5(data).hexdigest()

                hasher = hashlib.md5()
                f = open(file, "rb")
                buf = f.read(chunksize)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = f.read(chunksize)
                f.close()
                hName = hasher.hexdigest()
                hFileName = hDir + "/" + hName + ".txt"
                hf = open(hFileName, 'w').close()

            except MemoryError as e:
                print "*** MemoryError***"
                print "*** " + e.strerror
                print "*** " + file
                print "******************"
        else:
            if os.path.isdir(file):
                processDir(file)
            else:
                print "cas inattendu : " + file

hDir = "q:\input\hash"

if not os.path.exists(hDir):
    os.makedirs(hDir)
else:
    if not os.path.isdir(hDir):
        print hDir + " exists and is not a directory. Exiting."

processDir(".")
