import serial
import time

def relayOn():
  relayfile.setDTR(True)
  print 'on'

def relayOff():
  relayfile.setDTR(False)
  print 'off'

relayfile = serial.Serial('/dev/ttyUSB0', baudrate=9600)

while True:
  relayOn()
  time.sleep(1)
  relayOff()
  time.sleep(1)
  
