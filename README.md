
#How to install ES9018K2M_serial_sync on Raspberry Pi

This ES9018K2M_serial_sync is made by Audiophonics for the RaspDac-Touch devices.
The script send by serial the bitrate, volume, and audio filter.
The serial data look like this "A,X,X,X". 

Exp for a 16bit music at 50% of volume and filter 1: "A,0,50,1"

##For RuneAudio

###Get started:
Connect to your Raspberry Pi running RuneAudio by ssh using Putty or any ssh client

User: root, and password: rune

Exp on linux : ssh root@runeaudio.local

1. Install the lib:
	```
	pacman -Sy python2-pyserial pacman -S python2-mpd
	```

2. Edit config file:
	Edit the /boot/config.txt
	```
	nano /boot/config.txt
	```
	And uncomment #dtoverlay=hifiberry-dac\n
	Save the file with ctrl+o and exit with ctrl+x

3. Clone our github:
	```
	git clone https://github.com/audiophonics/ES9018K2M_serial_sync.git
	```

4. Install the script:
	```
	chmod 755 ES9018K2M_serial_sync/ES9018K2M_serial_sync.py
	mv ES9018K2M_serial_sync/ES9018K2M_serial_sync.py /usr/local/bin
	mv ES9018K2M_serial_sync/ES9018K2M_serial_sync.service /usr/lib/systemd/system/
	systemctl enable ES9018K2M_serial_sync
	rm -r ES9018K2M_serial_sync 
	```

Reboot your Raspberry Pi and select "hardware volume" in the "MPD" page of RuneAudio
