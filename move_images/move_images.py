# Import libraries
import os, shutil as sh

# Import source and destination variables
from my_directories import source, destination

# Variables for upper and lowercase of file extensions
p1 = '.png'
p2 = '.PNG'
j1 = '.jpg'
j2 = '.JPG'
je1 = '.jpeg'
je2 = '.JPEG'

def move_pics(files):
    '''
    go through file list
    check if file contains image extension
    if not, do nothing
    if yes, move it from source to directory
    '''
    for f in files:
        if p1 in f or p2 in f or j1 in f or j2 in f or je1 in f or je2 in f:
            sh.move(source + f, destination)

    return

# Get files from source
source_files = os.listdir(source)

# Call move pictures function to move pics from source to destination
move_pics(source_files)

# Message to user
print('\nPictures Successfully Moved')