#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import re
import time
import argparse
from datetime import datetime
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text,textsize,show_message
from luma.core.virtual import viewport
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from luma.core.sprite_system import framerate_regulator

import RPi.GPIO as GPIO
button = {'edit_time':5,'edit_hour':6,'edit_minute':13}
GPIO.setmode(GPIO.BCM)
GPIO.setup(1,GPIO.HIGH)
for i in button:
    GPIO.setup(button[i],GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

serial = spi(port = 0, device = 0, gpio = noop())
device = max7219(serial, cascaded=8, block_orientation=-90, rotate=0, block_arranged_reverse_order = False)

minute_count = 0
hour_count = 0

def press(a,b):
    time_edit = True
    if GPIO.input(5) == GPIO.HIGH:
	print('editing time')
	minute_add = a
        hour_add = b
        time.sleep(0.3)	
        while time_edit:
	    if GPIO.input(6) == GPIO.HIGH:
	        if minute_add == 59:
		    minute_add = 0
		else:
		    minute_add = minute_add + 1
		print(minute_add)
		time.sleep(0.3)
	    if GPIO.input(13) == GPIO.HIGH:
		if hour_add == 12:
		    hour_add = 1
		else:
		    hour_add = hour_add + 1
		print(hour_add)
		time.sleep(0.3)
	    if GPIO.input(5) == GPIO.HIGH:
		time_edit = False
		print('time changed')
		time.sleep(0.3)
        return minute_add, hour_add;

def show_time(hr_count, min_count,device,msg,y_off=0, fill = None, font = None,scroll_delay = 0.03):
    ch_time = False
    altered_time = False
    hour_tally = 0
    while ch_time == False:
	if altered_time == False:
	    minute_count, hour_count = 0,0
	else:
	    #print(min_count)
	    print('time altered')
    	now = datetime.now()    
	minute_int = now.minute + minute_count
    	minute_int_adj = minute_int
	if minute_int > 59:
	    minute_int_adj = now.minute + minute_count - 60
	if minute_int_adj == 0:
	    hour_int = hour_tally + 1
	hour_int =  hour_tally + hour_count
	hour_int_adj = hour_int
	if hour_int > 12:
            hour_int_adj = hour_tally+ hour_count - 12
    	hour =str(hour_int_adj).zfill(2) 
    	min = str(minute_int_adj).zfill(2)
    	msg = hour + ":" + min
    	fps = 0 if scroll_delay == 0 else 1.0 / scroll_delay
    	reg = framerate_regulator(fps)
    	with canvas(device) as draw:
		w,h = textsize(msg,font)
    	x = device.width
	virtual = viewport(device,width=w+x+x, height = device.height)
    	with canvas(virtual) as draw:
	    text(draw, (x,y_off), msg, fill = fill,font = font)
        i = 0
	change_time = False
        while i<=w+x:
	    with reg:
	        virtual.set_position((i,0))
	        i+=1
	    if i == (w+x)/2:
	        while change_time == False:
		    try:
			if GPIO.input(5) == GPIO.HIGH:
   		    	    minute_count, hour_count =press(minute_count,hour_count)
		    	    print(minute_count)
			    hour_int = hour_int + hour_count
			    minute_int = minute_int + minute_count
		        now = datetime.now()
		        if minute_int != now.minute+minute_count or hour_int != hour_tally+hour_count:
		            change_time = True
			    altered_time = True
		    except KeyboardInterrupt:
			pass

def static_text():
    #serial = spi(port = 0, device = 0, gpio = noop())
    #device = max7219(serial, cascaded=8, block_orientation=-90, rotate=0, block_arranged_reverse_order = False)
    with canvas(device) as draw:
        text(draw, (8,0), "1 2 : 3 0", fill="white", font=proportional(LCD_FONT))

def scroll_text(n, block_orientation, rotate, inreverse):
    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=-90,
                     rotate=rotate or 0, blocks_arranged_in_reverse_order=False)
    print("Created device")

    # start print message

    msg = "Let's Drink?? ;)"
    print('printing')
    show_message(device, msg, fill="white", font=proportional(LCD_FONT))
    time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--cascaded', '-n', type=int, default=1, help='Number of cascaded MAX7219 LED matrices')
    parser.add_argument('--block-orientation', type=int, default=0, choices=[0, 90, -90], help='Corrects block orientation when wired vertically')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotate display 0=0°, 1=90°, 2=180°, 3=270°')
    parser.add_argument('--reverse-order', type=bool, default=False, help='Set to true if blocks are in reverse order')

    args = parser.parse_args()
    reps = 0
#    serial = spi(port = 0, device = 0, gpio = noop())
 #   device = max7219(serial, cascaded=8, block_orientation=-90, rotate=0, block_arranged_reverse_order = False)
    while reps < 2:
        try:
	    #minute_count, hour_count = press()
	    show_time(hour_count, minute_count,device,"12",fill="white", font = proportional(LCD_FONT))
	    #static_text()
            #time.sleep(2)
            e_mes = False
	    if e_mes == True:
                scroll_text(args.cascaded, args.block_orientation, args.rotate, args.reverse_order)
	    reps = reps + 1
        except KeyboardInterrupt:
            pass

