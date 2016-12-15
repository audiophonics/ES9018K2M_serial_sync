
#How to install ES9018K2M_serial_sync for RuneAudio

##Get started:
Connecte to your Raspberry Pi running RuneAudio by ssh using Putty or any ssh client

User: root, and password: rune

Exp on linux : ssh root@runeaudio.local

1. Install lib:
	```
	pacman -Sy python2-pyserial pacman -S python2-mpd
	```

2. Edit config files:
	```
	nano /boot/config.txt and uncomment #dtoverlay=hifiberry-dac
	save the file with ctrl+o and exit with ctrl+x
	```

3. Clone our github:
	```
	git clone https://github.com/audiophonics/ES9018K2M_serial_sync.git
	```

4. Install the script:
	```
	chmod 755 ES9018K2M_serial_sync/ES9018K2M_serial_sync.py
	mv ES9018K2M_serial_sync/ES9018K2M_serial_sync.py /usr/local/bin
	mv ES9018K2M_serial_sync/ES9018K2M_serial_sync.service /usr/lib/systemd/system/ES9018K2M_serial_sync.service
	systemctl enable ES9018K2M_serial_sync
	```
