#!/usr/bin/env python

import csv
import json
import re
import traceback

import requests

import archivesspace_login as as_login


def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def run_query(api_url, headers, resource_uri, tc_data_sorted=None):
        try:
            query = f'{{"query":{{"jsonmodel_type": "field_query", "field": "collection_uri_u_sstr", "value": "{resource_uri}", "literal":true}}}}'
            tc_search = requests.get(api_url + "/repositories/12/top_containers/search?filter=" + query, headers=headers).json()
            tc_data = [[item['id'], json.loads(item['json'])['indicator']] for item in tc_search['response']['docs'] if 'response' in tc_search]
            tc_data_sorted = sorted(tc_data, key=lambda sublist: natural_key(sublist[1]))
        # this blanket except statement is not what you'd want to do if you were distributing this program, but 
        # works for this example since you will want to see what your errors are in order to fix them
        except Exception:
            print(traceback.format_exc())
        finally:
            return tc_data_sorted

def main():
    api_url, headers = as_login.login()
    csvpath = input('Please enter path to output CSV file: ')
    resource_uri = input('Please enter resource URI (i.e. /repositories/12/resources/11718): ')
    with open(csvpath, 'a', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['uri', 'old_box_number', 'new_box_number'])
        tc_data_output = run_query(api_url, headers, resource_uri)
        if tc_data_output is not None:
            csvwriter.writerows(tc_data_output)
        else:
            print('No results! Please check your data.')

if __name__ == "__main__":
    main()