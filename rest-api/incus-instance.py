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


class Instances:

  def __init__(self):
    self.r = ""

  def create(self, instance):
    for _ins in vdata:
      print(_ins)
      self.r = requests.post(url+"/instances", data=json.dumps(_ins), verify=False, headers=headers, cert=(clientCrt, clientKey))
    f.close()
    return self.r

  def stop(self, instance):
    self.r = requests.put(url+"/instances/"+instance+"/state", data=json.dumps(stop_instance), verify=False, headers=headers, cert=(clientCrt, clientKey))
    return self.r

  def start(self, instance):
    self.r = requests.put(url+"/instances/"+instance+"/state", data=json.dumps(start_instance), verify=False, headers=headers, cert=(clientCrt, clientKey))
    return self.r

  def delete(self, instance):
    self.r = requests.delete(url+"/instances/"+instance, data=json.dumps(payload), verify=False, headers=headers, cert=(clientCrt, clientKey))
    return self.r


def usage():
  print("./incus-instance.py -r create|start|stop|delete")
  return
  sys.exit(1)


def main():

  try:
    option, arguments = getopt.getopt(sys.argv[1:],"hcrsd:n",["help","create=","run=","stop=","delete=","number"])
  except getopt.GetoptError as error:
    print(error)
    sys.exit()


  for opt, arg in option:
    if opt in ("-h", "--help"):
      usage()
    elif opt in ('-c', '--create'):
        r = ins.create(arg)
    elif opt in ('-r', '--run'):
        r = ins.start(arg)
    elif opt in ('-s', '--stop'):
        r = ins.stop(arg)
    elif opt in ('-d', '--delete'):
        r = ins.delete(arg)
    else:
      usage()
      sys.exit()

  print(r.status_code)
  print(r.json())


if __name__ == '__main__':
    ins = Instances()
    main()

