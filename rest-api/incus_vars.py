clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url = "https://192.168.1.81:8443/1.0"
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}


attach_network = {

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

start_instance = {

  "action": "start",
  "timeout": 0,
  "force": False,
  "stateful": False

}

stop_instance = {

  "action": "stop",
  "timeout": -1,
  "force": False,
  "stateful": False

}

delete_instance = {

  "class": "task",
  "description": "Deleting instance",
  "status_code": 103,
  "resources": {
    "instances": [
      "/1.0/instances"
    ]
  },
  "metadata": "",
  "may_cancel": False,
  "err": ""

}

# https://linuxcontainers.org/incus/docs/main/howto/instances_create/

