# hello
# #https://stackoverflow.com/questions/16044229/how-to-get-keyboard-input-in-pygame
from pygame import mixer
import pygame

pygame.init()
mixer.init()

# we should change these to what we want them to be
KEYS_TO_NOTES = {
    'a': 'C1',
    's': 'D1',
    'd': 'E1',
    'f': 'F1',
    'g': 'G1',
    'h': 'A1',
    'j': 'B1',
    'w': 'C#1',
    'e': 'D#1',
    't': 'F#1',
    'y': 'G#1',
    'u': 'A#1',
    'k': 'C2',
    'l': 'D2',
    ';': 'E2',
    '4': 'F2',
    '6': 'G2',
    '+': 'A2',
    '-': 'B2',
    'i': 'C#2',
    'p': 'D#2',
    ']': 'F#2',
    '9': 'G#2',
    'J': 'A#2',
}

# program quits if the user presses keys not in the dictionaries
while True: 
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			note = mixer.Sound('sounds/' + KEYS_TO_NOTES[chr(event.key)] + ".wav")
			mixer.Sound.play(note)
			print(KEYS_TO_NOTES[chr(event.key)])
			# mixer.music.play()
			# mixer.find_channel().play(a3)
			# channel1.play()

			# if event.key == pygame.K_SPACE:
			# 	print("Space was pressed")
			# 	# mixer.music.stop()
			# 	mixer.pause()