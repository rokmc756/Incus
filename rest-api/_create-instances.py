#!/usr/bin/python3

import json
import requests
import urllib3
import logging


clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url = "https://192.168.1.81:8443/1.0/instances"
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}

payload = {

  # "source": {
  #  "alias": "hello-world",
  #  "protocol": "oci",
  #  "type": "image",
  #  "server": "https://docker.io"
  #}

  "architecture": "",
  "config": {},
  "devices": {},
  "ephemeral": False,
  "profiles": [
    "default"
  ],
  "stateful": False,
  "description": "",
  "name": "ubuntu-container",
  "source": {
    "type": "image",
    "certificate": "",
    "alias": "ubuntu/22.04",
    "server": "https://images.linuxcontainers.org",
    "protocol": "simplestreams",
    "mode": "pull",
    "allow_inconsistent": False
  },
  "instance_type": "",
  "type": "virtual-machine",        # "container",
  "start": True

}

urllib3.disable_warnings()
logging.captureWarnings(True)

# verify=certServer
r = requests.post(url, data=json.dumps(payload), verify=False, headers=headers, cert=(clientCrt, clientKey))

print(r.status_code)
print(r.json())

