import requests
from time import sleep
import os
import re

import Constants
from HelperFunctions import *

#Constants
##API KEY
mobsf_latest_image = "opensecurity/mobile-security-framework-mobsf:latest"
api_key_regex = "REST API Key: <strong><code>(.*)<\/code><\/strong>"
api_key = ''
container_states_tuple = ("running", "exited", "paused", "dead")

#status messages
#pull_successful = "Status: Downloaded newer"
#already_up_to_date = "Status: Image is up to date"

##Endpoint URLs
mobsf_url_and_endpoints = {
    "url": "http://localhost:8000/",
    "api_docs_endpoint": "http://localhost:8000/api_docs",
    "api_app_upload": "api/v1/upload",
    "api_app_scan": "api/v1/scan",
    "api_app_download_pdf": "api/v1/download_pdf",
    "api_app_report_json": "api/v1/report_json"
}
input_file = os.listdir(Constants.INPUT_FOLDER)[0]
report_directory = Constants.REPORT_FOLDER

mobsf_container_details = {
    'container_id': "",
    "container_name": "mobsf_security_tool",
    "container_state": ""
}

##Commands
mobsf_image_pull_command = f"docker pull {mobsf_latest_image}"
mobsf_run_container_command = f"docker run -d -p 8000:8000 --name {mobsf_container_details['container_name']} {mobsf_latest_image}"


def start_mobsf_server():
    # check if the mobsf container exists, else pull
    # check the status
    # if running call reachability check, else
    for container_state in container_states_tuple:
        mobsf_container_details['container_id'] = execute_shell_command(
            f"docker container ls -aqf name={mobsf_container_details['container_name']} -f status={container_state}")
        if mobsf_container_details['container_id']:
            mobsf_container_details['container_state'] = container_state
            print(f"{mobsf_container_details['container_name']} found in {container_state} state, with ID {mobsf_container_details['container_id']}")
            break

    try:
        if mobsf_container_details['container_id'] is "":
            print(f"No MobSF container found, pulling & running the latest mobsf image{mobsf_latest_image}")
            execute_shell_command(mobsf_run_container_command)
            start_mobsf_server()
        else:
             if (mobsf_container_details['container_state'] is "running") or (mobsf_container_details['container_state'] is "exited") or (mobsf_container_details['container_state'] is "paused"):
                if try_restarting_mobsf() is True:
                    print("Successfully launched & verified MobSF")
                else:
                    print(f"Failed restart of the MobSF server, please start the mobsf server manually")

    except Exception as error:
        print(error)
        return False

def try_restarting_mobsf():
    execution_output = execute_shell_command(f"docker container restart {mobsf_container_details['container_id']}")
    if execution_output in mobsf_container_details['container_id']:
        print(f"Restart command issued to the container without error")
        sleep(10)
    else:
        return False

    return verify_reachability_of_mobsf_url()

def verify_reachability_of_mobsf_url():
    try:
        global mobsf_url_and_endpoints
        check_request = requests.get(mobsf_url_and_endpoints['url'])
        if check_request.status_code == 200:
            return True
        else:
            print(f"{mobsf_url_and_endpoints['url']} not reachable")
            return False
    except Exception as error:
        print(f"Error encountered {mobsf_url_and_endpoints['url']} not reachable")
        return False

def extract_api_key_for_mobsf_remote_operations():
    try:
        api_docs_request = requests.get(mobsf_url_and_endpoints['api_docs_endpoint'])
        if api_docs_request.status_code == 200:
            print(f"{mobsf_url_and_endpoints['api_docs_endpoint']} exists..")
            global api_key
            api_key = re.findall(re.compile(api_key_regex), api_docs_request.content.decode('utf-8'))[0]
            print(f"retrieved MobSF API key : {api_key}")
        else:
            print(f"{mobsf_url_and_endpoints['api_docs_endpoint']} not reachable")
            return False
    except Exception as error:
        print(f"{error}")
        return False


def verify_api_test_call():
    pass

def upload_file_for_scan():
    pass

def scan_input_file():
    pass

def download_report_as_dictionary():
    pass

def download_report_as_PDF():
    pass

def clean_up():
    pass


extract_api_key_for_mobsf_remote_operations()
