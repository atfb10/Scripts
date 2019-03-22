'''
Import library that will allow opening of file in notepad from script
Enter assembly file to extract comments from
Enter text file to save comments to
Reads file line by line and if it contains comment sign it copies it into the file to be saved
Only takes comment aspect, not by using comment symbol ';' as delimeter
Saves comments to text file and opens file in notepad
'''
import webbrowser as wb

print('Enter assembly file to extract comments from', end=': ')
filepath = input() 
print('Enter text file name you would like extracted comments to be saved to', end=': ')
comment_file = input()

with open(filepath) as path:  
   for cnt, line in enumerate(path):
       if ';' in line:
           delimiter = ';'
           with open(comment_file + '.txt', 'a') as the_file:
                comment_only = ';' + line[line.index(delimiter) + len(delimiter):]
                the_file.write(comment_only)

print('Comments successfully written to file ' + comment_file + '.txt')
print('File opened in notepad')

wb.open(comment_file + '.txt')