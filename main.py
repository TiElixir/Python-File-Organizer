import os

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

        all_files.append(os.path.splitext(item))
print(all_files)

