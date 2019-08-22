import threading
import time
import cv2
import numpy as np
import paho.mqtt.client as mqtt
import serial
#import zbar
import sys, getopt
from PIL import Image
from paho.mqtt import publish
from video import create_capture
import serialtest
import pygame
import Adafruit_GPIO as GPIO
import Adafruit_CharLCD as LCD

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
ser = serial.Serial(
    "/dev/ttyAMA0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout=1,
    timeout=10,
    rtscts=False,
    dsrdtr=False,
    xonxoff=False)
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
 
# Set the height and width of the screen
size   = [400, 300]
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("consolas", 20)
 
pygame.display.set_caption("Game Title")
  
#Loop until the user clicks the close button.
done  = False
flag  = None
clock = pygame.time.Clock()
 
# print text function
def printText(msg, color='BLACK', pos=(50, 50)):
    textSurface      = font.render(msg, True, pygame.Color(color), None)
    textRect         = textSurface.get_rect()
    textRect.topleft = pos
 
    screen.blit(textSurface, textRect)
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we willimport Adafruit_GPIO as GPIO


    clock.tick(10)
     
    # Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.KEYDOWN: # If user release what he pressed.
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            flag = True
        elif event.type == pygame.KEYUP: # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:  # If user clicked close.
            done = True                 
 
     
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # Print red text if user pressed any key.
    if flag == True:
        printText('you just key down!!', 'RED')
        printText('--> you pressed any key.', 'RED', (50, 70))
        printText('Pressed Key : ' + buttons[0], 'RED', (50, 90))
        ser.write(buttons[0].encode())
        lcd.message(buttons[0])
 
    # Print blue text if user released any key.
    elif flag == False:
        printText('you just key up!!', 'BLUE')
        printText('--> released what you pressed.', 'BLUE', (50, 70))
 
    # Print default text if user do nothing.
    else:
        printText('Please press any key.')
 
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
'''
def keyboardinput(key): 
    #Loop until the user clicks the close button.
    flag  = None
    clock = pygame.time.Clock()
 
    while not key:
 
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
         
        # Main Event Loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.KEYDOWN: # If user release what he pressed.
                pressed = pygame.key.get_pressed()
                buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
                flag = True
            elif event.type == pygame.KEYUP: # If user press any key.
                flag = False
            elif event.type == pygame.QUIT:  # If user clicked close.
                done = True                 
     
        # Print red text if user pressed any key.
        if flag == True:
            print('Pressed Key : ')
            print(buttons[0])
                serialtest.sersend(buttons[0])
                break
        # Print blue text if user released any key.
        elif flag == False:
            print("key up")
        #    get_weight(img2, rad_curvature_value, center_offset)
        # Print default text if user do nothing.
        else:
            print("Please press any key.")
            
while 1:
   # Initialize the game engine
    pygame.init()
 
    # Set the height and width of the screen
    size   = [400, 300]
    screen = pygame.display.set_mode(size)
    
        #Loop until the user clicks the close button.
    flag  = None
    clock = pygame.time.Clock()
 
   
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
    # Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.KEYDOWN: # If user release what he pressed.
            pressed = pygame.key.get_pressed()
            buttons = [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            flag = True
        elif event.type == pygame.KEYUP: # If user press any key.
            flag = False
        elif event.type == pygame.QUIT:  # If user clicked close.
            done = True                 
     
        # Print red text if user pressed any key.
    if flag == True:
        print('Pressed Key : ')
        print(buttons[0])
#        if buttons[0]=='k':
#            k=0
#        else:
#            k=1       
#    keyboardinput(k)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #txt = 'Weight Value is ' + '{:04.2f}'.format(np.absolute(weight_value)) + ' on the ' + direction + ' direction '
    #cv2.putText(img, txt, (50,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
'''    
