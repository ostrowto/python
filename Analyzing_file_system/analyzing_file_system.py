#analyzing_file_system

import os, pathlib, sys

folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]


filepaths = [f.path for f in os.scandir('.') if f.is_file()]
dirpaths = [f.path for f in os.scandir('.') if f.is_dir()]

filepaths_as_string = str(filepaths)
dirpaths_as_string = str(dirpaths)

sys.stdout = open('Your_files_and_directories.txt', 'w')

for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        print('FILE__________: ', os.path.join(dirpath, f))
    for d in dirnames:
        print('DIRECTORY_____: ', os.path.join(dirpath, d))

sys.stdout.close()




