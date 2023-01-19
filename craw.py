# import os
# from tkinter import Tk
# from tkinter.filedialog import askdirectory

# def crawl_directory(path, file):
#     for dirpath, dirnames, filenames in os.walk(path):
#         for dirname in dirnames:
#             file.write("Directorio: " + os.path.join(dirpath, dirname) + "\n")
#         for filename in filenames:
#             file.write("Archivo: " + os.path.join(dirpath, filename) + "\n")

# root = Tk()
# root.withdraw()
# path = askdirectory()
# with open("output.txt", "w") as f:
#     crawl_directory(path, f)

# import os
# from tkinter import Tk
# from tkinter.filedialog import askdirectory

# def crawl_directory(path, file, level=0):
#     for dirpath, dirnames, filenames in os.walk(path):
#         for dirname in dirnames:
#             file.write("  "*level + "Directorio: " + os.path.join(dirpath, dirname) + "\n")
#             crawl_directory(os.path.join(dirpath, dirname), file, level+1)
#         for filename in filenames:
#             file.write("  "*level + "Archivo: " + os.path.join(dirpath, filename) + "\n")

# root = Tk()
# root.withdraw()
# path = askdirectory()
# with open("output.txt", "w") as f:
#     crawl_directory(path, f)

import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

def crawl_directory(path, file, level=0):
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            file.write("  "*level + "Directorio: " + os.path.join(dirpath, dirname) + "\n")
            crawl_directory(os.path.join(dirpath, dirname), file, level+1)
        for filename in filenames:
            file.write("  "*level + "Archivo: " + os.path.join(dirpath, filename) + "\n")

root = Tk()
root.withdraw()
path = askdirectory()
with open("output.txt", "w") as f:
    crawl_directory(path, f)

os.system("sudo pyinstaller --onefile craw.py")
os.system("sudo chmod +x dist/craw")
