#/usr/bin/python3

import csv
import json
import traceback

import requests

import archivesspace_login as as_login


def update_indicators(api_url, headers, row):
	#this is the first row of the spreadsheet
	archival_object_uri = row[0]
	# this is the seventh row of the spreadsheet
	old_folder_number = row[6]
	#this is the eight row of the spreadsheet
	new_folder_number = row[7]
	try:
		ao_json = requests.get(f"{api_url}/{archival_object_uri}", headers=headers).json()
		if 'error' in ao_json:
			print(archival_object_uri)
			print(row)
			print(ao_json)
		for instance in ao_json['instances']:
			if instance.get('instance_type') == 'mixed_materials':
				if instance.get('sub_container').get('indicator_2') == old_folder_number:
					instance['sub_container']['indicator_2'] = new_folder_number
		post_record = requests.post(f"{api_url}/{archival_object_uri}", headers=headers, json=ao_json).json()
		print(post_record)
	# this blanket except statement is not what you'd want to do if you were distributing this program, but 
	# works for this example since you will want to see what your errors are in order to fix them
	except Exception:
		print(archival_object_uri)
		print(row)
		print(traceback.format_exc())

def main():
	api_url, headers = as_login.login()
	csvpath = input('Please enter path to CSV file: ')
	with open(csvpath, 'r', encoding='latin-1') as csvfile:
		csvreader = csv.reader(csvfile)
		#skips the header row
		next(csvreader, None)
		try:
			for row in csvreader:
				update_indicators(api_url, headers, row)
		except Exception:
			print(row)
			print(traceback.format_exc())


if __name__ == "__main__":
	main()