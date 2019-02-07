# Import modules
import os

# Global variables
BAD_NAME = 'PNG'
GOOD_NAME = 'png'

#  Put current directory files in a list
fileList = os.listdir('.')

# Check each file in list. If one ends in .PNG, correct to .png.
for filename in fileList:
    if filename[-3:] == BAD_NAME:
        correctName = filename[:-3] + GOOD_NAME
        os.rename(filename, correctName)

# Ensure that no .PNG extensions escaped 
fileList = os.listdir('.')
for filename in fileList:
    if filename[-3:] == BAD_NAME:
        print(filename)

# Exit message
print('Files, successfully changed. Ensure correct spelling for each file in repo before submitting.')