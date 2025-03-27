clientCrt = "./incus-api.crt"
clientKey = "./incus-api.key"
url = "https://192.168.1.81:8443/1.0"
certServer = "./incus-api.pem"
headers = {'content-type': 'application/json'}

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

