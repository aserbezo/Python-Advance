import os

try:
    os.remove("my_first_file.txt")

except:
    print("File already deleted")
