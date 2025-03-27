#!/usr/bin/python3

import json
import requests
import urllib3
import logging


clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url = "https://192.168.1.81:8443/1.0/instances/ubuntu-container"
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}

payload = {

  #"architecture": "x86_64",
  #"config": {
  #  "image.architecture": "amd64",
  #  "image.description": "Ubuntu jammy amd64 (20250326_07:42)",
  #  "image.os": "Ubuntu",
  #  "image.release": "jammy",
  #  "image.serial": "20250326_07:42",
  #  "image.type": "disk-kvm.img",
  #  "image.variant": "default",
  #  "volatile.base_image": "b9f7ddfa399cc02736f2d71c5657e2b6c16e34454c68501826fc993272973070",
  #  "volatile.cloud-init.instance-id": "60f75014-8c10-4f28-9a97-93a5aed953c0",
  #  "volatile.last_state.power": "RUNNING",
  #  "volatile.uuid": "2ace1bfa-7318-4e53-aad2-df7f72603bb9",
  #  "volatile.uuid.generation": "2ace1bfa-7318-4e53-aad2-df7f72603bb9",
  #  "volatile.vsock_id": "2042328067"
  #},
  "devices": {
    "eth1": {
      "network": "jbr01",
      "type": "nic"
    }
  },
  "ephemeral": False,
  "profiles": [
    "default"
  ],
  "stateful": False,
  "description": ""

}


urllib3.disable_warnings()
logging.captureWarnings(True)

# verify=certServer
r = requests.post(url, data=json.dumps(payload), verify=False, headers=headers, cert=(clientCrt, clientKey))

print(r.status_code)
print(r.json())

