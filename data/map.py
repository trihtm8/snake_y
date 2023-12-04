import pygame
from pygame.locals import *

#define grid_pos_x (GPX) and grid_pos_y (GPY) for easy to call position in the maze
grid_pos_x=0
grid_pos_y=1
#a map is a rect size 800x600, with grid=20x20, we have 40x30 grid, 
#first col/line have id 0
#so
max_GP_X=39
max_GP_Y=29


#class save MAP info
class MAP():
	def __init__(seft, name, id):
		seft.name=name
		seft.id=id
		seft.bg_img="img/maps/"+str(seft.id)+"/map.png"
		seft.w_img="img/maps/"+str(seft.id)+"/wall.png"
		seft.maze=[] 
		#----maze is an array with (GPX,GPY)
		#values to choise where the wall place in the map.
		#----call: <Object>.maze[<index>][grid_pos_<x/y>]
	def name(seft):
		return seft.name
	def id(seft):
		return seft.id
	def set_maze(seft, new_maze): 
		seft.maze=new_maze


#funtions to design maze
def maze_rect_solid(maze, from_x, from_y, to_x, to_y):
	m=maze
	for i in range(from_x, to_x+1):
		for j in range(from_y, to_y+1):
			m.append((i,j))
	m=set(m)
	m=list(m)
	return m
	#line: maze_rect_solid(maze, from_x, line_y, to_x, line_y)
	#col: maze_rect_solid(maze, col_x, from_y, col_x, to_y)

def maze_del_solid(maze, from_x, from_y, to_x, to_y):
	m=maze
	for i in range(from_x, to_x+1):
		for j in range(from_y, to_y+1):
			try:
				m.remove((i,j))
			except:
				pass
	return m


#funtion to display map
def draw_MAP(SURFACE, mapx):
	CHOISE_MAP=pygame.image.load(mapx.bg_img)
	WALL=pygame.image.load(mapx.w_img)
	SURFACE.blit(CHOISE_MAP, (0,0))
	for w in range(len(mapx.maze)):
		SURFACE.blit(WALL, (25+mapx.maze[w][grid_pos_x]*20, mapx.maze[w][grid_pos_y]*20))



#2D array to colision check
MAP_2D_MAZE=[[0 for y in range(max_GP_Y+1)] for x in range(max_GP_X+1)]
#reset map_2D_maze to full 0 as begin state
def reset_2D_maze():
	for x in range(max_GP_X+1):
		for y in range(max_GP_Y+1):
			MAP_2D_MAZE[x][y] = 0
#set map_2D_maze[x][y] to 1 value if it is a wall in maze
def set_2D_maze(mapx):
	for m in mapx.maze:
		MAP_2D_MAZE[m[grid_pos_x]][m[grid_pos_y]]=1


#map lv1:
map1 = MAP("Back yard", 1)
map1_maze=[]
map1_maze=maze_rect_solid(map1_maze, 0,0,39,29)
map1_maze=maze_del_solid(map1_maze, 1,1,38,28)
map1_maze=maze_rect_solid(map1_maze, 17,4,17,4)
map1_maze=maze_rect_solid(map1_maze, 31,5,31,5)
map1_maze=maze_rect_solid(map1_maze, 11,7,11,7)
map1_maze=maze_rect_solid(map1_maze, 25,11,25,11)
map1_maze=maze_rect_solid(map1_maze, 6,11,6,11)
map1_maze=maze_rect_solid(map1_maze, 6,21,6,21)
map1_maze=maze_rect_solid(map1_maze, 36,14,36,14)
map1_maze=maze_rect_solid(map1_maze, 32,26,32,26)
map1_maze=maze_rect_solid(map1_maze, 11,26,11,26)
map1_maze=maze_rect_solid(map1_maze, 20,26,20,26)
map1_maze=maze_rect_solid(map1_maze, 26,20,26,20)
map1_maze=maze_rect_solid(map1_maze, 19,16,19,16)
map1.set_maze(map1_maze)

map2 = MAP("Zoo",2)
map2_maze=[]
map2_maze=maze_rect_solid(map2_maze, 0,0,39,29)
map2_maze=maze_del_solid(map2_maze, 1,1,38,28)
map2.set_maze(map2_maze)

map3 = MAP("City",3)
map3_maze=[]
map3_maze=maze_rect_solid(map3_maze, 0,0,39,29)
map3_maze=maze_del_solid(map3_maze, 1,1,38,28)
map3.set_maze(map3_maze)

def getmap(id):
	if id == 1:
		return map1
	elif id == 2:
		return map2
	elif id == 3:
		return map3

count=3
