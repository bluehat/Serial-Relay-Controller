import serial
import time
import urllib
import json

def relayOn():
  relayfile.setDTR(True)
  #print 'on'

def relayOff():
  relayfile.setDTR(False)
  #print 'off'

relayfile = serial.Serial('/dev/ttyUSB0', baudrate=9600)

def getUsers():
  userURL = urllib.urlopen('http://signup.hackerdojo.com/api/rfid')
  data = userURL.read()
  userURL.close()
  userData = json.loads(data)
  return userData

userData = getUsers()
for user in userData:
  print user['rfid_tag']

while True:
  key = raw_input('RFID?').strip()
  print key
  for user in userData:
     print user['rfid_tag']
     if key == user['rfid_tag']:
        foundUser = user
  
  if foundUser is not None:
    print 'hello ' + foundUser['username']
    relayOff()
    time.sleep(3)
    relayOn()
    foundUser = None
