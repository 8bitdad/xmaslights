#!/usr/bin/python

import RPi.GPIO as GPIO
import time

DELAY = 1

#
# GPIO signals for the 4 relays
#
# Note that there are enough GPIO signals to control multiple
#   4-channel boards from the same RPi
#
# Name the channels and note of the color of your wires for reference
#
CH1 = 23 # Channel 1 - Brown
CH2 = 22 # Channel 2 - Orange
CH3 = 27 # Channel 3 - Green
CH4 = 17 # Channel 4 - Yellow

#
# Setup the four channels with GPIO signals as output
# 
GPIO.setmode(GPIO.BCM)
GPIO.setup(CH1, GPIO.OUT)
GPIO.setup(CH2, GPIO.OUT)
GPIO.setup(CH3, GPIO.OUT)
GPIO.setup(CH4, GPIO.OUT)

#
# The sequence for the relay controller - bit mask of each
#    of the 4 channels. This example first turns each of the 
#    channels off, then cycles through each one, one at a time, 
#    and then repeats the sequence again
#
# Sequence table describes the order you want the lights to come on.
#
sequence = [0b0000,   # All off
            0b0001,   # Only channel 1 on
            0b0010,   # Only channel 2 on
            0b0100,   # Only channel 3 on
            0b1000]   # Only channel 4 on

#
# Start at the beginning of the sequence array
#
index = 0

#
# Run Forever...
#
while True:

    #
    #Convert the integer sequence bitmask into the individual
        #    channel controls
        GPIO.output(CH1, ((sequence[index] & 1) == 1))
        GPIO.output(CH2, ((sequence[index] & 2) == 2))
        GPIO.output(CH3, ((sequence[index] & 4) == 4))
        GPIO.output(CH4, ((sequence[index] & 8) == 8))

        #
        # Delay... make this as long as you want, or make it variable
        #
        time.sleep(DELAY)

        #
        # Advance to the next pattern in the sequence
        #
        index = index + 1
        if (index >= len(sequence)):
               index = 0
