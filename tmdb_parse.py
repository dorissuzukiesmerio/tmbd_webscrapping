import json # to parse the files
import pandas # read the csv
import glob # looping through all the files in a folder 
import os # do folder in operating system 

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


