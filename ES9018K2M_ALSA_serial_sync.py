#!/usr/bin/python2
# coding: utf-8
# AUDIOPHONICS ES9018K2M ALSA Serial Sync script
# http://www.audiophonics.fr/en/diy-dac/audiophonics-i-sabre-dac-es9018k2m-raspberry-pi-3-pi-2-a-b-i2s-p-11500.html
# Linked to ALSA card #1
# Change card number in line 25 if needed
# The audio data received by the DAC must not be affected by ALSA value

import time , serial
import subprocess
import os
from mpd import MPDClient

# MPD Bitrate
def MpdGetAudio(mpd):
        status = mpd.status()
        bitrate = status.get('audio')
	if (bitrate):
		audiotab = bitrate.split(':')
        	if (audiotab[1] == "16"):
# Always return 1 if using RPI-DAC driver (24bit fixed)
                	return ("A,0")
        return ("A,1") 

# Realtime Biterate card 1
def Getbitrate():
	with open("/proc/asound/card1/pcm0p/sub0/hw_params","r") as fichier:
		for i in range(2):
			bitread = fichier.readline()
	bitrate = bitread[9:11]
	if (bitrate == "16"):
# DESACTIVER ETAT 0 SI RPI-DAC (24bit)
			return ("A,0")
	return ("A,1") 		
		

# MPD Volume
def MpdGetVolume(mpd):
        status = mpd.status()
        volume = status.get('volume')
        return (volume)

#ALSA Mixer Volume
def Getvolume():
        amixervol = "amixer | tail -1 | cut -d'[' -f2 | cut -d '%' -f1"
	process = subprocess.Popen(amixervol, stdout=subprocess.PIPE , shell=True)
	os.waitpid(process.pid, 0)[1]
	volcut = process.stdout.read().strip()
	volume = volcut[0:12]		
        return (volume)		

		

if __name__ == '__main__':
        MPD_HOST = 'localhost'
        MPD_PORT = '6600'
        ser = serial.Serial('/dev/ttyS0', 2400)
        mpd = MPDClient()
        filtre = "1"
	
	mpd.connect(MPD_HOST, MPD_PORT)
	try:
        	while True:
			bitrate = Getbitrate()
                        #print (bitrate)
                        volume = Getvolume()
                        #print (volume)
                        send = str(bitrate) + "," + str(volume) + "," + str(filtre)
                        ser.write(send.encode('utf-8'))
			print(send)
                	time.sleep(0.1)
	except KeyboardInterrupt:
	        mpd.close()
		mpd.disconnect()
mpd.close()
mpd.disconnect()

