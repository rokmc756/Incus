#!/bin/bash

curl -X "POST" -k "https://192.168.1.81:8443/1.0/instances" \
     --cert ./incus-api.crt --key ./incus-api.key \
     -d $'{
  "source": {
    "alias": "hello-world",
    "protocol": "oci",
    "type": "image",
    "server": "https://docker.io"
  }
}'


