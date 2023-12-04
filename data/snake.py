import pygame
from pygame.locals import *

class SNAKE:
	def __init__(seft, id):
		seft.id=id
		seft.bd_img="img/snakes/"+str(id)+"/body.png"
		seft.hu_img="img/snakes/"+str(id)+"/head_up.png"
		seft.hd_img="img/snakes/"+str(id)+"/head_down.png"
		seft.hl_img="img/snakes/"+str(id)+"/head_left.png"
		seft.hr_img="img/snakes/"+str(id)+"/head_right.png"
		seft.maze=[(1,1), (2,1), (3,1)]
		seft.prec="right"
	def auto_move(seft):
		for x in range(len(seft.maze)-1):
			seft.maze[x]=seft.maze[x+1]
		if (seft.prec == "up"):
			seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0], seft.maze[len(seft.maze)-1][1]-1)
		elif (seft.prec == "down"):
			seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0], seft.maze[len(seft.maze)-1][1]+1)
		elif (seft.prec == "left"):
			seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0]-1, seft.maze[len(seft.maze)-1][1])
		elif (seft.prec == "right"):
			seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0]+1, seft.maze[len(seft.maze)-1][1])
	def move_up(seft):
		for x in range(len(seft.maze)-1):
			seft.maze[x]=(seft.maze[x+1][0],seft.maze[x+1][1])
		seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0], seft.maze[len(seft.maze)-1][1]-1)
		seft.prec="up"
	def move_down(seft):
		for x in range(len(seft.maze)-1):
			seft.maze[x]=(seft.maze[x+1][0],seft.maze[x+1][1])
		seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0], seft.maze[len(seft.maze)-1][1]+1)
		seft.prec="down"
	def move_left(seft):
		for x in range(len(seft.maze)-1):
			seft.maze[x]=(seft.maze[x+1][0],seft.maze[x+1][1])
		seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0]-1, seft.maze[len(seft.maze)-1][1])
		seft.prec="left"
	def move_right(seft):
		for x in range(len(seft.maze)-1):
			seft.maze[x]=(seft.maze[x+1][0],seft.maze[x+1][1])
		seft.maze[len(seft.maze)-1]=(seft.maze[len(seft.maze)-1][0]+1, seft.maze[len(seft.maze)-1][1])
		seft.prec="right"
	def head_pos(seft):
		return seft.maze[len(seft.maze)-1]
	def reset(seft):
		seft.maze=[(1,1), (2,1), (3,1)]
		seft.prec="right"
	def eat(seft, prec):
		hp=seft.head_pos()
		if prec=="up":
			check_pos=(hp[0], hp[1]-1)
		elif prec=="down":
			check_pos=(hp[0], hp[1]+1)
		elif prec=="left":
			check_pos=(hp[0]-1, hp[1])
		elif prec=="right":
			check_pos=(hp[0]+1, hp[1])
		seft.maze.append(check_pos)
		seft.prec=prec


def draw_SNAKE(SURFACE, snakex):
	CHOISE_BODY=pygame.image.load(snakex.bd_img)
	CHOISE_HEAD_UP=pygame.image.load(snakex.hu_img)
	CHOISE_HEAD_DOWN=pygame.image.load(snakex.hd_img)
	CHOISE_HEAD_LEFT=pygame.image.load(snakex.hl_img)
	CHOISE_HEAD_RIGHT=pygame.image.load(snakex.hr_img)
	for w in range(len(snakex.maze)-1):
		SURFACE.blit(CHOISE_BODY, (25+snakex.maze[w][0]*20, snakex.maze[w][1]*20))
	if (snakex.prec == "up"):
		SURFACE.blit(CHOISE_HEAD_UP, (25+snakex.maze[len(snakex.maze)-1][0]*20, snakex.maze[len(snakex.maze)-1][1]*20))
	elif (snakex.prec == "down"):
		SURFACE.blit(CHOISE_HEAD_DOWN, (25+snakex.maze[len(snakex.maze)-1][0]*20, snakex.maze[len(snakex.maze)-1][1]*20))
	elif (snakex.prec == "left"):
		SURFACE.blit(CHOISE_HEAD_LEFT, (25+snakex.maze[len(snakex.maze)-1][0]*20, snakex.maze[len(snakex.maze)-1][1]*20))
	elif (snakex.prec == "right"):
		SURFACE.blit(CHOISE_HEAD_RIGHT, (25+snakex.maze[len(snakex.maze)-1][0]*20, snakex.maze[len(snakex.maze)-1][1]*20))


snake1 = SNAKE(1)
snake2 = SNAKE(2)
snake3 = SNAKE(3)

def get_snake(id):
	if id == 1:
		return snake1
	if id == 2:
		return snake2
	if id == 3:
		return snake3

count=3