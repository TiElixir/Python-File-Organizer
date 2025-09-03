import os
import shutil as sh

pathInitialized=False

while pathInitialized==False:
    pathToSort=input("Enter the path you want to sort: ")
    if os.path.isdir(pathToSort):
        break
    else:
        print("Invalid Path!")

all_items=os.listdir(pathToSort)
all_files=[]
for item in all_items:
    if os.path.isfile(os.path.join(pathToSort,item)):

        all_files.append(item)

extensions=[]
extentions_unique={}
diction={'Image': ['.png', '.jpg', '.jpeg', '.bmp', '.webp'], 'Video':['.mp4', '.mkv', '.mov'], 'Audio':['.mp3', '.wav', '.ogg']}

for file in all_files:
    extensions.append(os.path.splitext(file)[-1])

extensions_unique=set(extensions)
fileCatPair=[]

def cat(x):
    extn=os.path.splitext(x)[-1]

    
    for key, value in diction.items():
        if extn in value:
            return(key)

for file in all_files:
    try:
        if os.path.isdir(os.path.join(pathToSort,cat(file))):
            a=0
        else:
            os.makedirs(os.path.join(pathToSort,cat(file)))
            sh.move(os.path.join(pathToSort,file),os.path.join(pathToSort,cat(file),file))
    except:
        continue
        