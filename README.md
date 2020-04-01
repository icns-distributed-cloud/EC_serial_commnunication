# Set up Raspberry Pi Serial Communication
###Introduction
EC_serial_communication allows Raspberry pi to establish serial communication.
For serial communication, Raspberry pi requires several settings.
We use a pypnut module to display the status of the communication on the screen.
More details are described below.
## Enable serial in raspi-config
## In case of RPi3, the bluetooth is communicating with the uart, so you must stop the bluetooth
## Therefore, make the following settings.
### 1) pi@raspberrypi:~$ sudo nano /boot/config.txt
###    - dtoverlay=pi3-disable-bt
### 2) stop uart between bluetooth chips
###    - pi@raspberrypi:~$ sudo systemctl disable hciuart
### 3) Disable Console
###   - pi@raspberrypi:~$ sudo vi /boot/cmdline.txt

Modify this section as follows.

#dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait

->

dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait

I referred to the blog below.

http://blog.naver.com/PostView.nhn?blogId=windi97&logNo=220913135183&parentCategoryNo=&categoryNo=50&viewDate=&isShowPopularPosts=true&from=search
