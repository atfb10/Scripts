# Freeze excel panes

### Background 
- Often I work with large and long Excel files
- It is useful to be able to be able to see column headings when thousands of rows down page
- This script will make "sticky headers" for all excel files in a folder
- Meaning, as you scroll the header will at top of cells visible as you scroll

### Instructions 
- Place file in desired directory
- Open Excel files in directory and place cursor on cell "A1" and save file
- Navigate to the directory in your terminal
- Run the script by typing the following command "py freeze_excel_panes.py"
- Open the excel files, accept recovery. Note: no error, just doesn't like the code affecting the workbook
- Save the excel file
- Rerun script whenever a new workbook is added to the repository


### Warning
- This particular script is created to only work with workbooks with single sheets
- If used in a directory with workbooks of multiple sheets, it will simply work only for the first sheet
- Only works with workbooks ending in .xlsx file extension