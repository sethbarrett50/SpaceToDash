'''
Created by Seth Barrett

This project is designed to change any file names with spaces to a -

-----------------------------------------------------------------------
Import Statements to Import Used Modules
-----------------------------------------------------------------------
'''
import os
'''
-----------------------------------------------------------------------
Opening Message
-----------------------------------------------------------------------
'''
print(f'\n{"":-^60}\n{"Space to - Converter ":-^60}\n{"For File Management":-^60}\n{"Created by Seth Barrett":-^60}\n{"King":-^60}\n{"":-^60}')
'''
-----------------------------------------------------------------------
Show Current Working Directory, Ask for Input and Choose Directory
-----------------------------------------------------------------------
'''
boolUI = False
ufolder = ''
while not boolUI:
    print(f'Current Working Directory:{os.getcwd()}')
    dirs = [ f for f in os.listdir( os.curdir ) if os.path.isdir(f) ]
    for dir in dirs:
        print(f'{"-"*5}{dir}')
    uifolder = str(input('Please choose the directory wish that contains all the files to be converted:'))
    if uifolder in dirs:
        ufolder = uifolder
        boolUI = True
        break
    print(f'\n{"":-^60}Type a correct directory\'s name.\n{"":-^60}')
'''
-----------------------------------------------------------------------
Rename all files with names containing spaces
-----------------------------------------------------------------------
'''
rnfiles = []
for root, dirpath, files in os.walk(ufolder):
    for file in files:
        if (file.__contains__(' ')):
            rnfiles.append(file)
            rnfile = file.replace(' ', '-')
            os.rename(os.path.join(root, file), os.path.join(root, rnfile))
'''
-----------------------------------------------------------------------
Exit Message
-----------------------------------------------------------------------
'''
print(f'{"":-^60}\nThe files that were renamed were: {rnfiles}\n{"":-^60}\n{"End of Space to - Converter":-^60}\n{"":-^60}')

