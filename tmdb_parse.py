import json # to parse the files
import pandas # read the csv
import glob # looping through all the files in a folder 
import os # do folder in operating system 

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

json_file_name = "json_files/tmdb550.json"
f = open(json_file_name, "r")
json_data = json.load(f)
f.close()

# print(json_data)

# Nested structure:

print(json_data['adult'])
print(json_data['backdrop_path'])
