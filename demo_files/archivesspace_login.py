#/usr/bin/python3

import json
import requests
import traceback


def send_login_request(url=None, username=None, password=None):
    """Logs into the ArchivesSpace API"""
    try:
        if url is None and username is None and password is None:
            url = input('Please enter the ArchivesSpace API URL: ')
            username = input('Please enter your username: ')
            password = input('Please enter your password: ')
        auth = requests.post(url+'/users/'+username+'/login?password='+password).json()
        #if session object is returned then login was successful; if not it failed.
        if 'session' in auth:
            session = auth["session"]
            h = {'X-ArchivesSpace-Session':session, 'Content_Type': 'application/json'}
            print('Login successful!')
            return (url, h)
        else:
            print('Login failed! Check credentials and try again.')
            print(traceback.format_exc())
            #try again
            u, heads = login()
            return u, heads
    except:
        print('Login failed! Check credentials and try again!')
        print(traceback.format_exc())
        u, heads = send_login_request()
        return u, heads


def login():
    '''Loads the configuration file and logs in to the ArchivesSpace API, returning the API URL and an authorization key to be used in requests'''
    config_file = json.load(open("config.json"))
    return send_login_request(url=config_file['api_url'], username=config_file['api_username'], password=config_file['api_password'])
