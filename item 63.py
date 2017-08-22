import os
import shutil

source = ("C:\\Users\Student\Desktop\FolderA\\")
destination = ("C:\\Users\Student\Desktop\FolderB\\")

for filename in os.listdir(source):
    shutil.move( source + filename, destination)
    print(destination + filename)
