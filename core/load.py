import os
import json

def load (foldername) :
  jdata = {}
  for filename in os.listdir(f'{foldername}'):
    if filename[-5::]  == '.json':
        with open ( f'{foldername}/{filename}' , 'r', errors='replace') as jfile:
            print (jfile)
            jdata_unit = json.load(jfile)
            jdata.update(jdata_unit)
  return (jdata)

if __name__ == "__main__":
    print (load(input()))