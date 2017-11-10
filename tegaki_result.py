#!/usr/bin/python3

# Imports
import base64
import json
import requests
import os
import csv

TEGAKI_FORM_ENDPOINT = 'https://api.tegaki.ai/hwr/v1/form'
MY_API_KEY = '***'
PROXIES = {
        'http': 'http://***',
        'https': 'https://***',
        }
REQ_RESULT_FILE_NAME = "results.txt"
IMAGE_DIR = "C:\\Users\\Takeshi_Umezaki\\Documents\\ocr\\"

_json_str = ""
_request_id = ""
_dict_response = ""

 
# base64-encoding files

# Get results from an already send request using the id
def get_result(request_id):
    # Build the endpoint with the request id
    endpoint = TEGAKI_FORM_ENDPOINT + '/' + request_id

    # Send GET request
    response = requests.get(endpoint, headers={'Authorization': 'apikey {}'.format(MY_API_KEY)})

    # Print the result
    # print(_response)
    return response.json()


# Get results from an already send request using the id
def get_result_text(dict_field):
    if dict_field.get("singleLine") != None:
        result_text = dict_field["singleLine"]["text"]
    if dict_field.get("boxedCharacters") != None:
        result_text = dict_field["boxedCharacters"]["text"]
    return result_text


if __name__ == '__main__':
    print("start")
    os.chdir(IMAGE_DIR)
    with open(REQ_RESULT_FILE_NAME, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row[0] + "," + row[1])
            _request_id = row[1]
            dict_response = get_result(_request_id)
            print(type(dict_response))
            # names = dict_response["results"]["fields"]["name"]
            fields = dict_response["results"]["fields"]
            for field in fields:
                print(str(field.get("name")) + "," + get_result_text(field))
            
            # break

