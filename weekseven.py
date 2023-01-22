import os

if os.path.exists("newFile.txt"):
    os.remove("newFile.txt")
else:
    print("The File does not exist")

