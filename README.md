# recover-nero-backitup-nco-files
Recover old backup files from Nero Backitup

# What is it?
#This script runs recursive through a folder looking for .nco files

# Why?
#These .nco files are created by Nero BackitUp around the year 2004.
#You can use 7-zip for it, stated on the nero website, but it is easier to run this script.

# How it Works:
#Folders are respected, original file names are recovered and after unzipping the file the .nco file will be removed.

# How to use:
Edit the line directory = 'path_to_nco_files' and point it to a folder where the script can look for .nco files
I used Python 3.11.0 but this script is so simple, any version of Python should work.
