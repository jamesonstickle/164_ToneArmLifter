#!/usr/bin/python
 
import sys
import usb.core
import requests
import time
import datetime
import subprocess
 
streams="Sound Level Meter:i"
tokens=""
 
dev=usb.core.find(1a2c:2c27)
 
assert dev is not None
 
print dev
 
print hex(dev.idVendor)+','+hex(dev.idProduct)
 
#create the first file in which to save the sound level readings
sound_level_filepath = "/home/pi/Documents/sound_level_records/"
now_datetime_str = time.strftime("%Y_%m_%d_%H_%M",datetime.datetime.now().timetuple())
sound_level_file = open(sound_level_filepath + now_datetime_str,"w")
 
while True:
#every minute create a new file in which to save the sound level readings
now_datetime = datetime.datetime.now()
if (now_datetime.second == 0): #(now_datetime.minute == 0) and:
sound_level_file.close
now_datetime_str = time.strftime("%Y_%m_%d_%H_%M",now_datetime.timetuple())
sound_level_file = open(sound_level_filepath + now_datetime_str,"w")
time.sleep(1)
ret = dev.ctrl_transfer(0xC0,4,0,0,200)
dB = (ret[0]+((ret[1]&amp;amp;amp;3)*256))*0.1+30
print time.strftime("%Y_%m_%d_%H_%M_%S",now_datetime.timetuple()) + "," + str(dB)
sound_level_file.write(time.strftime("%Y_%m_%d_%H_%M_%S",now_datetime.timetuple()) + "," + str(dB) + "\n")
