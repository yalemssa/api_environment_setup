#/usr/bin/python3

import csv
import json
import requests
import archivesspace_login as as_login




def opencsv(input_csv=None):
    """Opens a CSV in reader mode."""
    try:
        if input_csv is None:
            input_csv = input('Please enter path to CSV: ')
        if input_csv == 'quit':
            quit()
        file = open(input_csv, 'r', encoding='utf-8')
        csvin = csv.reader(file)
        headline = next(csvin, None)
        return headline, csvin
    except:
        logging.exception('Error: ')
        logging.debug('Trying again...')
        print('CSV not found. Please try again. Enter "quit" to exit')
        h, c = opencsv()
        return h, c


config_file = json.load("config.json")
api_url, headers = as_login.login()
header_row, csvfile = opencsv(config_file['input_csv'])

for row in csvfile:
	