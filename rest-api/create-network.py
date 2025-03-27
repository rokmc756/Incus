#!/usr/bin/python3

import json
import requests
import urllib3
import logging


clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url = "https://192.168.1.81:8443/1.0/networks"
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}

payload = {

  "config": {},
  "description": "test",
  "name": "jbr01",
  "type": "bridge",
  "project": "default"

}

urllib3.disable_warnings()
logging.captureWarnings(True)

r = requests.post(url, data=json.dumps(payload), verify=False, headers=headers, cert=(clientCrt, clientKey))
print(r.status_code)
print(r.json())

