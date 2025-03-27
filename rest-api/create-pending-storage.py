#!/usr/bin/python3

import json
import requests
import urllib3
import logging


clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url_prefix = "https://192.168.1.81:8443/1.0/storage-pools?target="
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}
hosts = ['ubt24-node01', 'ubt24-node02', 'ubt24-node03', 'ubt24-node04', 'ubt24-node05']

payload = {

  "config": {},
  "description": "",
  "name": "jzfs-pool01",
  "driver": "zfs"

}

urllib3.disable_warnings()
logging.captureWarnings(True)

for h in hosts:
    url = url_prefix + h
    r = requests.post(url, data=json.dumps(payload), verify=False, headers=headers, cert=(clientCrt, clientKey))
    print(r.status_code)
    print(r.json())

