# ES9018K2M_serial_sync
ES9018K2M Serial Sync for PI2 PI3 

//Update Kernel
pacman -Sy --force raspberrypi-firmware-bootloader linux-raspberrypi

//Install lib:
pacman -Sy pacman -S python2-pyserial pacman -S python2-mpd

//Edit config files:  
Open /boot/config.txt: nano /boot/config.txt  

add "#dtoverlay=pi3-disable-bt-overlay" by "dtoverlay=pi3-disable-bt-overlay" 
add enable_uart=1  

Save file
Open /boot/cmdline.txt:  
remove "console=ttyAMA0,115200" and "kgdboc=ttyAMA0,115200"  Save file

Save file
