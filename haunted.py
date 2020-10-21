# C code for Arduino translated to this Python file for the Raspberry Pi
# taken from original project here - thank you oneguyoneblog: 
# https://oneguyoneblog.com/2017/11/01/lightning-thunder-arduino-halloween-diy/
# This project requires a Raspbery Pi SenseHat or replace it with your own
# Light system

import random
from sense_hat import SenseHat
import pygame
import time

sense = SenseHat()
sense.clear()

pygame.mixer.init()
pygame.mixer.music.set_volume(100.0)

def allOn(brightness):
	white = [brightness, brightness, brightness] 
	for x in range(0, 7):
		for y in range(0, 7):
			sense.set_pixel(x, y, white)

def delay(millis):
    time.sleep(.001 * millis)

def allOff():
	sense.clear()

while True:

    flashCount = random.randrange(3, 15)    # Min. and max. number of flashes each loop

    flashBrightnessMin =  10                # LED flash min. brightness (0-255)
    flashBrightnessMax =  255               # LED flash max. brightness (0-255)

    flashDurationMin = 1                    # Min. duration of each seperate flash
    flashDurationMax = 50                   # Max. duration of each seperate flash

    nextFlashDelayMin = 1                   # Min, delay between each flash and the next
    nextFlashDelayMax = 150                 # Max, delay between each flash and the next

    thunderDelay = random.randrange(500, 3000)  # Min. and max. delay between flashing and playing sound
    thunderFile = random.randrange(1, 17)       # There are 17 soundfiles: 0001.mp3 ... 0017.mp3
    loopDelay = random.randrange(3000, 7000)   # Min. and max. delay between each loop

    print("Flashing count: " + str(flashCount))

    for flash in range(0, flashCount):      # Flashing LED strip in a loop, random count

        allOn(random.randrange(flashBrightnessMin, flashBrightnessMax))     # Turn LED strip on, random brightness

        delay(random.randrange(flashDurationMin, flashDurationMax))     # Keep it tured on, random duration

        allOff()

        delay(random.randrange(nextFlashDelayMin, nextFlashDelayMax))   # Random delay before next flash

    print("Pausing before playing thunder sound, milliseconds: " + str(thunderDelay))

    delay(thunderDelay)

    thunderFile = str(random.randrange(16) + 1) + ".mp3"

    print("Playing thunder sound, file number: " + thunderFile)

    pygame.mixer.music.load(thunderFile)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:    # Wait to finish playing the MP3 file
        pass

    print("Pausing before next loop, milliseconds: " + str(loopDelay))

    delay(loopDelay)
