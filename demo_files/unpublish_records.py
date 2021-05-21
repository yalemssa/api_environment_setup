#/usr/bin/python3
#~/anaconda3/bin/python

#This script unpublishes records based on a list of URIs

import csv
import json
import logging
import os
import sys
import traceback
import requests

import archivesspace_login as as_login

def error_log():
    if sys.platform == "win32":
        log_file = '\\Windows\\Temp\\error_log.log'
    else:
        log_file = 'error_log.log'
    logging.basicConfig(filename=log_file, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    return log_file


def unpublish_recs(api_url, headers, row):
    logger = error_log()
    try: 
        record_uri = row[0]
        record_json = requests.get(f"{api_url}{record_uri}", headers=headers).json()
        if 'error' in record_json:
            logging.debug(f"Could not retrieve {record_uri}")
            logging.debug(record_json.get('error'))
        else:
            record_json['publish'] = False
            record_update = requests.post(f"{api_url}{record_uri}", headers=headers, json=record_json).json()
            if 'error' in record_update:
                logging.debug(f"Could not update {record_uri}")
                logging.debug(record_update.get('error'))
                print(record_update)
    except Exception as exc:
        logging.debug(record_uri)
        logging.exception('Error: ')
        print(record_uri)
        print(traceback.format_exc())

def main():
    api_url, headers = as_login.login()
    csvpath = input('Please enter path to CSV file: ')
    with open(csvpath, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        #skips the header row
        next(csvreader, None)
        for row in csvreader:
            unpublish_recs(api_url, headers, row)

if __name__ == "__main__":
    main()
