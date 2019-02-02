'''
Background:
A professor at Missouri S&T occasionally requires images to included for assignments
Assignments are cloned from GitLab, completed, and the altered and new files pushed to the remote branch
This professor has a script that performs unit tests, and checks for certain file names
The file names are specific, and must match the requirements exactly.
When saving a screenshot the image is regularly saved as .PNG
Which is the correct file extension, however it must be .png for his script to pick it up
Otherwise, points are lost
When run this file will check all files in its immediate directory
Any file that ends in .PNG will be changed to .png as to not lose points

Run Instructions: 
Place file in desired directory
Navigate to directory file resides in
Run the script: py lower_case_png_files.py
Files with .PNG will be changed to .png
'''

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