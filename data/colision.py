import data.map
import data.snake
import random
import pygame
from pygame.locals import *

def check_eat(snakex, food_pos, prec):
	hp=snakex.head_pos()
	if prec=="up":
		check_pos=(hp[0], hp[1]-1)
	elif prec=="down":
		check_pos=(hp[0], hp[1]+1)
	elif prec=="left":
		check_pos=(hp[0]-1, hp[1])
	elif prec=="right":
		check_pos=(hp[0]+1, hp[1])
	if check_pos == food_pos:
		return True
	return False

def check(MAP_2D_MAZE, snakex, prec):
	hp=snakex.head_pos()
	if prec=="up":
		check_pos=(hp[0], hp[1]-1)
	elif prec=="down":
		check_pos=(hp[0], hp[1]+1)
	elif prec=="left":
		check_pos=(hp[0]-1, hp[1])
	elif prec=="right":
		check_pos=(hp[0]+1, hp[1])
	if MAP_2D_MAZE[check_pos[0]][check_pos[1]]==1: #if check_pos is a wall
		return False
	for x in range(len(snakex.maze)-1):
		if (snakex.maze[x][0]==check_pos[0] and snakex.maze[x][1]==check_pos[1]):
			return False
	return True

def check_food(MAP_2D_MAZE, snakex, food_pos):
	if MAP_2D_MAZE[food_pos[0]][food_pos[1]] == 1:
		return False
	for x in range(len(snakex.maze)-1):
		if (snakex.maze[x][0]==food_pos[0] and snakex.maze[x][1]==food_pos[1]):
			return False
	return True

def randFood(MAP_2D_MAZE, snakex):
	food_pos = (random.randint(0,39), random.randint(0,29))
	while not check_food(MAP_2D_MAZE, snakex, food_pos):
		food_pos = (random.randint(0,39), random.randint(0,29))
	return food_pos

def draw_FOOD(SURFACE, food_pos):
	pygame.draw.circle(SURFACE, (255,0,255), (25+food_pos[0]*20+10, food_pos[1]*20+10), 10)