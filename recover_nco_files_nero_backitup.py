#What is it?
#This script runs recursive through a folder looking for .nco files

#Why?
#These .nco files are created by Nero BackitUp around the year 2004.
#You can use 7-zip for it, stated on the nero website, but it is easier to run this script.

#How it Works:
#Folders are respected, original file names are recovered and after unzipping the file the .nco file will be removed.

import os
import shutil
import zipfile
from pathlib import Path

directory = 'path_to_nco_files'
 
from glob import glob
for x in os.walk(directory):
    d = x[0]
    files = x[2]
    for f in files:
        z = os.path.join(d, f)
        file_extension = (os.path.splitext(z))[1]
        if file_extension == ".nco":
            with zipfile.ZipFile(z) as zip_file:
                for member in zip_file.namelist():
                    filename = os.path.basename(member)
                    # skip directories
                    if not filename:
                        continue
                
                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(member)
                    filename = Path(z).stem
                    target = open(os.path.join(d, filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
            print ("recovered " + z)
            os.remove(z)