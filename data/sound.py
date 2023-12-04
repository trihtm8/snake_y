import pygame
from pygame.locals import *
from pygame.mixer import *

pygame.init()
pygame.mixer.init()

music = pygame.mixer.Sound("sound/music/ForestWalk.mp3")
playingMusic=False

def playMusic():
	global playingMusic
	if not playingMusic:
		music.play(-1)
		playingMusic=True

def stopMusic():
	global playingMusic
	if playingMusic:
		music.stop()
		playingMusic=False



moveSound = pygame.mixer.Sound("sound/effect/waterdrop.wav")

def playMS():
	moveSound.play(0)

eatSound = pygame.mixer.Sound("sound/effect/chewing.wav")

def playE():
	eatSound.play(0)
