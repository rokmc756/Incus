#!/usr/bin/python3

import json
import requests
import urllib3
import logging
import sys,getopt

from incus_vars import *

f = open('./instances.json')
vdata = json.load(f)

urllib3.disable_warnings()
logging.captureWarnings(True)


class Networks:

  def __init__(self):
    self.r = ""

  def attach(self, instance):
    self.r = requests.post(url+"/instances/"+instance, data=json.dumps(attach_network), verify=False, headers=headers, cert=(clientCrt, clientKey))
    return self.r


def usage():
  print("./attach-network.py -a create|start|stop|delete")
  sys.exit(1)


def main():

  try:
    option, arguments = getopt.getopt(sys.argv[1:],"ha:n",["help","attach=","number"])
  except getopt.GetoptError as error:
    print(error)
    sys.exit()

  for opt, arg in option:
    if opt in ("-h", "--help"):
      usage()
    elif opt in ('-a', '--attach'):
        r = ins.create(arg)
    else:
      usage()
      sys.exit()

  print(r.status_code)
  print(r.json())


if __name__ == '__main__':
    ins = Networks()
    main()

