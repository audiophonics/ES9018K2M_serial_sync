#!/usr/bin/python2
# coding: utf-8

# Audiophonics 2016 Serial Driver for mpd
# ES9018K2M product page: http://www.audiophonics.fr/fr/dac-diy/audiophonics-i-sabre-dac-es9018k2m-raspberry-pi-3-pi-2-a-b-i2s-p-11500.html
# Made by Fujitus
#
# For RuneAudio
serial_port = '/dev/ttyS0'
# For MoodeAudio
#serial_port = '/dev/serial0'
# IF using RPI-DAC driver
#driver = "A,1"
# IF using Hifiberry driver
driver = "A,0"

import time , serial
from mpd import MPDClient

def MpdGetAudio(mpd):
        global driver
        status = mpd.status()
        bitrate = status.get('audio')
	if (bitrate):
		audiotab = bitrate.split(':')
        	if (audiotab[1] == "16"):
                	return (driver)
        return ("A,1")

def MpdGetVolume(mpd):
        status = mpd.status()
        volume = status.get('volume')
        return (volume)

if __name__ == '__main__':
        MPD_HOST = 'localhost'
        MPD_PORT = '6600'
        ser = serial.Serial(serial_port, 2400)
	ser.isOpen()
        mpd = MPDClient()
        filtre = 1
	last_send = "A,0,0,0"

	mpd.connect(MPD_HOST, MPD_PORT)
	try:
        	while True:
			bitrate = MpdGetAudio(mpd)
			time.sleep(0.1)
                        volume = MpdGetVolume(mpd)
                        send = str(bitrate) + "," + str(volume) + "," + str(filtre)
			if (send != last_send):
				print(send)
				last_send = send
	                        ser.write(send.encode('utf-8'))
	except KeyboardInterrupt:
	        mpd.close()
		mpd.disconnect()
mpd.close()
mpd.disconnect()
