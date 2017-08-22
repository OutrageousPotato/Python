import os
import shutil
import datetime

source = ("C:\\Users\Student\Desktop\FolderX\\")
destination = ("C:\\Users\Student\Desktop\FolderY\\")

now = datetime.datetime.now()
last24 = now-datetime.timedelta(hours=24)

for filename in os.listdir(source):
    stats = os.stat(source+filename)
    lastMod = datetime.datetime.fromtimestamp(stats[8])
    if(lastMod >= last24):
        print(lastMod)
        shutil.move( source + filename, destination)
        print(destination + filename)
