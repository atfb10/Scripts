# Libraries
import openpyxl, os

#  Put current directory files in a list
dirFileList = os.listdir('.')

# Create list to hold all python files 
excelFiles = []

# Add each excel file to excel file list
for file in dirFileList:
    if file[-4:] == 'xlsx':
        excelFiles.append(file)

# Set the sticky header for each file in the excel list file
for workbook in excelFiles:
    wb = openpyxl.load_workbook(workbook)
    sheet = wb.active
    sheet.freeze_panes = 'A2'
    wb.save(workbook)
