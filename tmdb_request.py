# print("Hello")

import urllib.request
import os 
import json
import time

f = open("api_key", "r")
api_key = f.read()
f.close()

# print(api_key) # This is 

if not os.path.exists("json_files"):
	os.mkdir("json_files")

response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/?api_key=" + api_key)
json_response = json.load(response)
movie_end = int(json_response['id']) 

movie_start = movie_end - 10

for movie_id in range(movie_start, movie_end):
	# movie_id = 550 # used only for one (while seeing if the code is working, before putting for loop for all)
	response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key)

	# print(response.read()) # taking a look : it is json, so instead of using this, use json library

	json_response = json.load(response)

	f = open("json_files/tmdb" + str(movie_id) + ".json", "w")
	f.write(json.dumps(json_response))
	f.close()
	time.sleep(20) # in practice, put larger number


# https://jsonformatter.org/json-pretty-print # 
