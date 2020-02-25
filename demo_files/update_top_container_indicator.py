#/usr/bin/python3

import json
import traceback

import requests

import archivesspace_login as as_login


api_url, headers = as_login.login()
csvpath = input('Please enter path to CSV file: ')

with open(csvpath, 'r', encoding='utf-8') as csvfile:
	csvreader = csv.reader(csvfile)
	#skips the header row
	next(csvreader, None)
	for row in csvreader:
		#this is the first row of the spreadsheet
		top_container_uri = row[0]
		#this is the third row of the spreadsheet
		new_box_number = row[2]
		try:
			top_container_json = requests.get(f"{api_url}/{top_container_uri}", headers=headers).json()
			top_container_json['indicator'] = new_box_number
			post_record = requests.post(f"{api_url}/{top_container_uri}", headers=headers, json=top_container_json).json()
			print(post_record)
		# this blanket except statement is not what you'd want to do if you were distributing this program, but 
		# works for this example since you will want to see what your errors are in order to fix them
		except:
			print(traceback.format_exc())
			continue