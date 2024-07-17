from pathlib import Path
import os
import shutil

SourcePath = str(input("Enter Path of Source: ")) 
p = Path(SourcePath) #Write Path to Location from where you need to get files to move

while True:
    if p.exists():
        print("Source Path Opened")
        break
    else:
        SourcePath = str(input("ReEnter Path Of Source: "))
        p = Path(SourcePath)

DescPath = str(input("Enter The Destination Path: "))

move_dir = Path(DescPath) #Directory where it is being moved


if not move_dir.exists():
    os.mkdir(move_dir)
else:
    print("Folder has been created already")

fileExtension = str(input("Enter file extension(eg: *.pdf here remember to add * before the extension, you could also specifiy FileName*.extension): "))

for filename in p.glob(fileExtension): # in glob you need to add the file extension

    #shows file name
    print(filename)
    #Creates a new name without suffix eg you have a pdf file you remove the .pdf from it
    newname = filename.with_suffix('')

    #creates the location path where the file needs to be stored
    locationPath = Path(move_dir / newname.name) 
    print(locationPath)

    if locationPath.exists() == None:
        os.mkdir(locationPath)
        shutil.move(filename,locationPath)
    else:
        shutil.move(filename,locationPath)