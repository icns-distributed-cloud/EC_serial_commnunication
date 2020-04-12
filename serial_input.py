import serial
import time
from pynput import keyboard,mouse


ser=serial.Serial("/dev/serial0",115200)
ser.timeout=0.1

if ser.isOpen():
    print("Serial is Open")

def on_press(key):
    ser.write('{}'.format(key).encode())
    ser.flush()
    print('key {} pressed'.format(key))
        
def on_release(key):
    if key==keyboard.Key.esc:
        return False
    
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
