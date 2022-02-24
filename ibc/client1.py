from genericpath import exists
import os
import sys
import json
import time

import pathlib
import urllib
import requests
import subprocess

import urllib3
import certifi

from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(category=InsecureRequestWarning)


class IBClient():  # automated login process for the paper trading account , for regular trading we can't do it because the 2 auth process.

    def __init__(self, username=None, password=None, account=None):  # dunder method

            # Initializes a new IB Client Object with the username and password of the account holder

        self.ACCOUNT = account
        self.USERNAME = username
        self.PASSWORD = password
        self.CLIENT_PORTAL_FOLDER = pathlib.Path.cwd().joinpath(
            'clientportal.gw').resolve()  # clientportal.beta.gw
        self.API_VERSION = 'v1/'

            # operation attributes
        self.TESTINT_FLAG = False
        self._operating_system = sys.platform
        self.server_process = self._server_state(action='load')
        self.authenticated = False

        # define url componets

        IB_GATEWAY_HOST = r"https://localhost"
        IB_GATEWAT_PORT = r"5000"
        self.IB_GATEWAY_PATH = IB_GATEWAY_HOST + ":" + IB_GATEWAT_PORT
        self.BACKUP_GATEWAY_PATH = r"https://cdcdyn.interactivebrokeres.com/portal.proxy"

    def _server_state(self, action='save'):

            # define file components - build the file path

        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = 'server_session.json'
        file_path = os.path.join(dir_path, file_name)
        file_exists = os.path.exists(file_path)

        # handle the case to save the session

        if action == 'save':
            with open(file_path, 'w') as server_file:
                json.dump({'server_process_id': self.server_process}, server_file)

    # handle the case to load an existing session  CHECK!!!!!!!!! BUGS !! 

        elif action == 'load' and file_exists:

                with open(file_path, 'r') as server_file: 
                     server_state = json.load(server_file)

                proc_id = server_state['server_process_id']

        if self._operating_system == 'win32':
            for process in os.popen('tasklist').read().splitlines()[4:]:
                if str(proc_id) in process:
                   process_details = process.split()
                   return proc_id
            else:
                try: 
                    os.kill(proc_id, 0)
                    return proc_id
                except OSError:
                    return None
                       
    # handle the case to close an existing session
    
        elif action == 'delete' and file_exists:
            os.remove(file_path)

        else:
             return None

# Create the headers for the request.

def _headers(self, mode = 'json'):

    if mode == 'json':
        headers = {'Content-type':'application/json'}
    elif mode == 'form':
           headers = {'Content-type': 'application/x-www-form-urlencoded'}

 # Build the full URL for a given request 

    def _build_url(self, endpoint = None):

        return urllib.parse.unquote(urllib.parse.urljoin(self.IB_GATEWAY_PATH, self.API_VERSION) + r'/portal/' + endpoint)

    def _make_request(self, endpoint = None, req_type = None, params = None):

 # Handle all the requests made by the client library

 # first build the url 

        url = self.build_url(endpoint = endpoint)

        # Scenario 1 POST with arguments 

        if req_type == 'POST' and params is not None:

            # Make sure we have headers for Json data.
            headers = self._headers()

            # Make the request and grab the response 
            response = requests.post(url = url, headers = headers, verify = False, data = json.dumps(params))

        elif req_type == 'POST' and params is None:

            # Make sure we have headers for JSON data.
            headers = self._headers()

            # Make the request and grab the response 
            response = requests.post(url = url, headers = headers, verify = False)

        elif req_type == 'GET' and params is not None:

            # Make sure we have headers for JSON data.
            headers = self._headers()

            # Make the request and grab the response 
            response = requests.get(url = url, headers = headers, verify = False, params = params)

        elif req_type == 'GET' and params is None:

            # Make sure we have headers for JSON data.
            headers = self._headers()

            # Make the request and grab the response 
            response = requests.get(url = url, headers = headers, verify = False)

   # Check the status code 
        if response.status_code != 200 and response.status_code !=201:
            print(response.url)
            print(response.headers)
            print(response.content)
            print(response.status_code)

        else: 

            return response 







         
