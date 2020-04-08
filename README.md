# Set up Raspberry Pi Serial Communication
## 1. Introduction
EC_serial_communication allows Raspberry pi 3 to establish serial communication with stm32f4discovery board.
(It can also communicate with other boards.)
For serial communication, Raspberry pi requires several settings.
We use a pypnut module to display the status of the communication on the screen.
More details are described below.
## 2. Configuration
### 1) Enable GPIO serial port
The GPIO serial port is disabled by default. In order to enable it, edit config.txt.

    $ sudo nano /boot/config.txt

and add the line at the bottom:

    enable_uart=1
### 2) Disable serial console
You need to disable serial console to use serial port.

    $ sudo systemctl stop serial-getty@ttyS0.service
    $ sudo systemctl disable serial-getty@ttyS0.service

You also need to remove the console from the cmdline.txt. 

    $ sudo vi /boot/cmdline.txt

and you will see the following comment.

    dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes root wait

Then, remove the line:

    console=serial0,115200

(You can also do the same thing on the interface.)

### 3) Swap the serial ports
To use the high performance serial port /dev/ttyAMA0, you can assign miniuart(/dev/ttys0) for bluetooth.

    $ sudo nano /boot/config.txt

and add:

    dtoverlay=pi3-miniuart-bt

You can check that it has worked by:

    $ ls -l /dev

    (before)
    serial0 -> ttyS0
    serial1 -> ttyAMA0

    (after)
    serial0 -> ttyAMA0
    serial1 -> ttyS0

reference : https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3-4/