import pygame
from pygame.locals import *
import sys

import data
from data import map
from data import snake
from data import colision
from data import level
from data import sound
from data import score

#set enviroment
pygame.init()
pygame.font.init()
DISPLAYSURF = pygame.display.set_mode((850,650))
pygame.display.set_caption('Snake_y game')
FPS=60
fpsClock=pygame.time.Clock()
#done

#color
white = (255,255,255)
black = (0,0,0)
gray = (100,100,100)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yelow = (255,255,0)
#end color

#set surfaces
	#design MAIN_MENU surface, load imgs
MAIN_MENU = pygame.Surface((850,650))
MAIN_MENU.fill(white)
		#set menu backgroud
menu_bg = pygame.image.load("img/surfaces/main_menu/menu.png") 
		#load hightlights button
play_HL_img = pygame.image.load("img/surfaces/main_menu/play_light.png")
option_HL_img = pygame.image.load("img/surfaces/main_menu/option_light.png")
		#load audio button
audio_img = pygame.image.load("img/surfaces/main_menu/audio.png")
mute_img = pygame.image.load("img/surfaces/main_menu/mute.png")


OPTION = pygame.Surface((850,650))
OPTION.fill(gray)
option_main_img=pygame.image.load("img/surfaces/option/option.png")
arrow_left_HL_img=pygame.image.load("img/surfaces/option/arrow_left_light.png")
arrow_right_HL_img=pygame.image.load("img/surfaces/option/arrow_right_light.png")
arrow_up_HL_img=pygame.image.load("img/surfaces/option/arrow_up_light.png")
arrow_down_HL_img=pygame.image.load("img/surfaces/option/arrow_down_light.png")

GAME_PLAY = pygame.Surface((850,650))
GAME_PLAY.fill(green)
#done

#-----Main menu: open first in play software, in this, choise option button to go option surface, 
#     or play button to play, or click at audio to mute, unmute
#-----Option: choise speed of snake, choise maps, see hightscore
#-----Gameplay: play game hear

#MAIN_MENU:
#class to display main menu
class Display_MAIN_MENU:
	def __init__(seft):
		seft.option_HightLight = False
		seft.play_HightLight = False
		seft.score_HightLight = False
		seft.mute = False
	def option_HL(seft):
		seft.option_HightLight = True
	def option_unHL(seft):
		seft.option_HightLight = False
	def play_HL(seft):
		seft.play_HightLight = True
	def play_unHL(seft):
		seft.play_HightLight = False
	def score_HL(seft):
		seft.score_HightLight = True
	def score_unHL(seft):
		seft.score_HightLight = False
	def muteThis(seft):
		seft.mute = True
	def unmuteThis(seft):
		seft.mute = False
	def reset(seft):
		seft.option_HightLight = False
		seft.play_HightLight = False
		seft.mute = False
#funtion set what to show on MAIN_MENU surface, use Display_MAIN_MENU_hander
def display_MN(Display_MAIN_MENU_hander):
	MAIN_MENU.blit(menu_bg, (0,0))
	if Display_MAIN_MENU_hander.play_HightLight == True:
		MAIN_MENU.blit(play_HL_img, (185,365))
	elif Display_MAIN_MENU_hander.option_HightLight == True:
		MAIN_MENU.blit(option_HL_img, (185,205))
	if Display_MAIN_MENU_hander.mute == True:
		MAIN_MENU.blit(mute_img, (440,500))
	elif Display_MAIN_MENU_hander.mute == False:
		MAIN_MENU.blit(audio_img, (440,500))
	menu_font=pygame.font.Font('GENSHIN.ttf',30)
	game_mode_text=menu_font.render(game_mode,True,(255,0,0))
	MAIN_MENU.blit(game_mode_text, (624,410))
	if Display_MAIN_MENU_hander.score_HightLight == True:
		score_btn_color=(255,255,0)
	else:
		score_btn_color=(255,0,0)
	score_btn_text=menu_font.render("Score", True, score_btn_color)
	MAIN_MENU.blit(score_btn_text, (630,250))

#funtion check if mouse move in button, use to highlight button and check click at where
def mouse_Move_In(x_min, y_min, x_max, y_max):
	mouse_x, mouse_y = pygame.mouse.get_pos()
	if (mouse_x>=x_min and mouse_x<=x_max and mouse_y>=y_min and mouse_y<=y_max):
		return True
	else:
		return False
 
#state on open sofware, change state to change windown you want to show
state = "main_menu"

#creat handeres
Display_MAIN_MENU_hander = Display_MAIN_MENU()

#class to display OPTION surface
class Display_OPTION:
	def __init__(seft):
		seft.speed=1
		seft.snake_id=1
		seft.map_id=1
		seft.back_menu_HightLight=False
		seft.arrow_left_HightLight=False
		seft.arrow_right_HightLight=False
		seft.arrow_up_HightLight=False
		seft.arrow_down_HightLight=False
		seft.snake_change_up_HightLight=False
		seft.snake_change_down_HightLight=False

	def reset(seft):
		seft.speed=1
		seft.snake_id=1
		seft.map_id=1
		seft.back_menu_HightLight=False
		seft.arrow_left_HightLight=False
		seft.arrow_right_HightLight=False
		seft.arrow_up_HightLight=False
		seft.arrow_down_HightLight=False
		seft.snake_change_up_HightLight=False
		seft.snake_change_down_HightLight=False

	def level_mode(seft, now_level):
		seft.speed=level.levels[now_level]['speed']
		seft.map_id=level.levels[now_level]['map']

	def change_snake(seft, id):
		seft.snake_id=id
	def change_map(seft, id):
		seftmap_id=id

	def back_menu_HL(seft):
		seft.back_menu_HightLight=True
	def back_menu_unHL(seft):
		seft.back_menu_HightLight=False

	def arrow_left_HL(seft):
		seft.arrow_left_HightLight=True
	def arrow_left_unHL(seft):
		seft.arrow_left_HightLight=False

	def arrow_right_HL(seft):
		seft.arrow_right_HightLight=True
	def arrow_right_unHL(seft):
		seft.arrow_right_HightLight=False

	def arrow_up_HL(seft):
		seft.arrow_up_HightLight=True
	def arrow_up_unHL(seft):
		seft.arrow_up_HightLight=False

	def arrow_down_HL(seft):
		seft.arrow_down_HightLight=True
	def arrow_down_unHL(seft):
		seft.arrow_down_HightLight=False

	def snake_change_up_HL(seft):
		seft.snake_change_up_HightLight=True
	def snake_change_up_unHL(seft):
		seft.snake_change_up_HightLight=False

	def snake_change_down_HL(seft):
		seft.snake_change_down_HightLight=True
	def snake_change_down_unHL(seft):
		seft.snake_change_down_HightLight=False

def display_OP(Display_OPTION_hander):
	map.draw_MAP(OPTION, map.getmap(Display_OPTION_hander.map_id))
	OPTION.blit(option_main_img, (100,0))
	if Display_OPTION_hander.arrow_left_HightLight==True:
		OPTION.blit(arrow_left_HL_img, (170,250))
	if Display_OPTION_hander.arrow_right_HightLight==True:
		OPTION.blit(arrow_right_HL_img, (600,250))
	if Display_OPTION_hander.arrow_up_HightLight==True:
		OPTION.blit(arrow_up_HL_img,(540,390))
	if Display_OPTION_hander.arrow_down_HightLight==True:
		OPTION.blit(arrow_down_HL_img,(540,440))
	if Display_OPTION_hander.back_menu_HightLight==True:
		OPTION.blit(arrow_left_HL_img,(116,13))
	if Display_OPTION_hander.snake_change_up_HightLight==True:
		OPTION.blit(arrow_up_HL_img,(541,503))
	if Display_OPTION_hander.snake_change_down_HightLight==True:
		OPTION.blit(arrow_down_HL_img,(541,553))
	show_option_font=pygame.font.Font('GENSHIN.ttf',30)
	show_map_text=show_option_font.render('Map '+str(Display_OPTION_hander.map_id)+': '+map.getmap(Display_OPTION_hander.map_id).name, True, (200,0,0))
	OPTION.blit(show_map_text, (260,280))
	show_speed_text=show_option_font.render('Speed: '+str(Display_OPTION_hander.speed)+' amps', True, (200,0,0))
	OPTION.blit(show_speed_text, (260, 410))
	show_snake=pygame.Surface((110,50))
	show_snake.fill((255,255,255))
	snake.draw_SNAKE(show_snake,snake.get_snake(Display_OPTION_hander.snake_id))
	OPTION.blit(show_snake, (350,520))
	show_snake_text=show_option_font.render('Snake:', True, (200,0,0))
	OPTION.blit(show_snake_text, (260,525))



Display_OPTION_hander=Display_OPTION()	

#class to control game
class GAME_Control:
	def __init__ (seft, speed, snakex, mapx):
		seft.choise_snake=snakex
		seft.choise_map=mapx
		seft.speed=speed
		map.reset_2D_maze()
		map.set_2D_maze(seft.choise_map)
		seft.food_pos=colision.randFood(map.MAP_2D_MAZE, snakex)
		#for game over
		seft.game_over_menu_HightLight=False
		seft.game_over_retry_HightLight=False
		seft.game_over_save_Disabled=False
		seft.game_over_save_HightLight=False
		#for cỏngatulation
		seft.congratulation_menu_HightLight=False
		seft.congratulation_retry_HightLight=False
	def go_menu_HL(seft):
		seft.game_over_menu_HightLight=True
	def go_menu_unHL(seft):
		seft.game_over_menu_HightLight=False
	def go_retry_HL(seft):
		seft.game_over_retry_HightLight=True
	def go_retry_unHL(seft):
		seft.game_over_retry_HightLight=False
	def go_disable(seft):
		seft.game_over_save_Disabled=True
	def go_enable(seft):
		seft.game_over_save_Disabled=False
	def go_save_HL(seft):
		seft.game_over_save_HightLight=True
	def go_save_unHL(seft):
		seft.game_over_save_HightLight=False
	def c_menu_HL(seft):
		seft.congratulation_menu_HightLight=True
	def c_menu_unHL(seft):
		seft.congratulation_menu_HightLight=False
	def c_retry_HL(seft):
		seft.congratulation_retry_HightLight=True
	def c_retry_unHL(seft):
		seft.congratulation_retry_HightLight=False
	def reset(seft):
		seft.choise_snake.reset()
		seft.food_pos=colision.randFood(map.MAP_2D_MAZE, seft.choise_snake)
		seft.game_over_menu_HightLight=False
		seft.game_over_retry_HightLight=False
		seft.congratulation_menu_HightLight=False
		seft.congratulation_retry_HightLight=False


def display_GAME(Display_GAME_hander):
	map.draw_MAP(GAME_PLAY, Display_GAME_hander.choise_map)
	snake.draw_SNAKE(GAME_PLAY, Display_GAME_hander.choise_snake)
	colision.draw_FOOD(GAME_PLAY, Display_GAME_hander.food_pos)
	game_font=pygame.font.Font('GENSHIN.ttf',30)
	score_text=game_font.render('Score: '+str(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed),True,color_By_Map(Display_GAME_hander.choise_map.id))
	GAME_PLAY.blit(score_text, (50,600))
	global game_mode
	if game_mode=="option":
		mode_text=game_font.render('Mode: Option',True,color_By_Map(Display_GAME_hander.choise_map.id))
	elif game_mode=="level":
		mode_text=game_font.render('Level: '+str(now_level)+'/'+str(level.max_level),True,color_By_Map(Display_GAME_hander.choise_map.id))
	GAME_PLAY.blit(mode_text, (300,600))
	map_text=game_font.render('Map: '+Display_GAME_hander.choise_map.name,True,color_By_Map(Display_GAME_hander.choise_map.id))
	GAME_PLAY.blit(map_text, (600,600))

def color_By_Map(map_id):
	match map_id:
		case 1:
			return (255,0,100)
		case 2:
			return (255,0,255)
		case 3:
			return (0,255,0)

#at game over
def display_GAME_OVER(Display_GAME_hander):
	game_over_img=pygame.image.load("img/surfaces/game_over.png")
	GAME_PLAY.blit(game_over_img,(176,133))
	go_font=pygame.font.Font('GENSHIN.ttf',30)
	score_text=go_font.render('Your score: '+str(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed),True,(200,0,0))
	GAME_PLAY.blit(score_text, (270,295))
	retry_color=(245,132,34)
	if Display_GAME_hander.game_over_retry_HightLight:
		retry_color=(245,245,34)
	menu_color=(245,132,34)
	if Display_GAME_hander.game_over_menu_HightLight:
		menu_color=(245,245,34)
	retry_text=go_font.render('Retry',True,retry_color)
	menu_text=go_font.render('Menu',True,menu_color)
	GAME_PLAY.blit(retry_text, (270,405))
	GAME_PLAY.blit(menu_text, (436,405))
	save_color=(110,110,110)
	if not Display_GAME_hander.game_over_save_Disabled:
		save_color=(245,132,34)
		if Display_GAME_hander.game_over_save_HightLight:
			save_color=(245,245,34)
	save_text=go_font.render("Save", True, save_color)
	GAME_PLAY.blit(save_text, (176+180,133+332))


def display_CONGRATULATION(Display_GAME_hander):
	congratulation_img=pygame.image.load("img/surfaces/congratulation.png")
	GAME_PLAY.blit(congratulation_img,(176,133))
	go_font=pygame.font.Font('GENSHIN.ttf',30)
	score_text=go_font.render('Your score: '+str(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed),True,(200,0,0))
	GAME_PLAY.blit(score_text, (270,295))
	retry_color=(245,132,34)
	if Display_GAME_hander.congratulation_retry_HightLight:
		retry_color=(245,245,34)
	menu_color=(245,132,34)
	if Display_GAME_hander.congratulation_menu_HightLight:
		menu_color=(245,245,34)
	retry_text=go_font.render('Retry',True,retry_color)
	menu_text=go_font.render('Menu',True,menu_color)
	GAME_PLAY.blit(retry_text, (270,405))
	GAME_PLAY.blit(menu_text, (436,405))
	if not Display_GAME_hander.game_over_save_Disabled:
		save_color=(245,132,34)
		if Display_GAME_hander.game_over_save_HightLight:
			save_color=(245,245,34)
	save_text=go_font.render("Save", True, save_color)
	GAME_PLAY.blit(save_text, (176+180,133+332))
#for game mode:
game_mode="option"

def change_game_mode():
	global game_mode
	if game_mode=="option":
		game_mode="level"
	elif game_mode=="level":
		game_mode="option"

now_level=0
now_score=0

#start game loop
frame_count=0
sound.playMusic()
while True:
	for event in pygame.event.get():
		if event.type == QUIT: #check QUIT event
			pygame.quit()
			sys.exit()

		if state == "main_menu":
			#get events at main_menu windown and change Display_MAIN_MENU_hander

			#hightlight the button if mouse_Move_In this, if move out, un hightlight
			if mouse_Move_In(180, 200, 600, 300):
				Display_MAIN_MENU_hander.option_HL()
			else:
				Display_MAIN_MENU_hander.option_unHL()
			if mouse_Move_In(180, 360, 600, 460):
				Display_MAIN_MENU_hander.play_HL()
			else:
				Display_MAIN_MENU_hander.play_unHL()
			if mouse_Move_In(617,248,735,296):
				Display_MAIN_MENU_hander.score_HL()
			else:
				Display_MAIN_MENU_hander.score_unHL()

			#on click events
			if event.type == MOUSEBUTTONDOWN:
				#if click at option or play button, change state to show another windown
				if mouse_Move_In(180, 200, 600, 300):
					state = "option"
					Display_MAIN_MENU_hander.option_unHL()
				elif mouse_Move_In(180, 360, 600, 460):
					frame_count=0
					state = "game"
					Display_MAIN_MENU_hander.play_unHL()
					if game_mode=="level":
						now_level=1
						Display_OPTION_hander.level_mode(now_level)
					Display_GAME_hander=GAME_Control(Display_OPTION_hander.speed, snake.get_snake(Display_OPTION_hander.snake_id), map.getmap(Display_OPTION_hander.map_id))
				elif mouse_Move_In(616,360,740,460):
					change_game_mode()
				#if click at audio symbol, change to mute if un_muting, and change to unmute if muting
				if mouse_Move_In(400, 500, 500, 600):
					if Display_MAIN_MENU_hander.mute == False:
						Display_MAIN_MENU_hander.muteThis()
						sound.stopMusic()
					else:
						Display_MAIN_MENU_hander.unmuteThis()
						sound.playMusic()
				#if click at score button, show score
				if mouse_Move_In(617,248,735,296):
					score.show_score(DISPLAYSURF)

		if state == "option":
			#get events at option windown and change Display_OPTION_hander
			if mouse_Move_In(170,250,225,350):
				Display_OPTION_hander.arrow_left_HL()
			else:
				Display_OPTION_hander.arrow_left_unHL()
			if mouse_Move_In(607,253,661,358):
				Display_OPTION_hander.arrow_right_HL()
			else:
				Display_OPTION_hander.arrow_right_unHL()
			if mouse_Move_In(540,390,607,431):
				Display_OPTION_hander.arrow_up_HL()
			else:
				Display_OPTION_hander.arrow_up_unHL()
			if mouse_Move_In(540,440,607,481):
				Display_OPTION_hander.arrow_down_HL()
			else:
				Display_OPTION_hander.arrow_down_unHL()
			if mouse_Move_In(116,13,166,110):
				Display_OPTION_hander.back_menu_HL()
			else:
				Display_OPTION_hander.back_menu_unHL()
			if mouse_Move_In(540,503,607,545):
				Display_OPTION_hander.snake_change_up_HL()
			else:
				Display_OPTION_hander.snake_change_up_unHL()
			if mouse_Move_In(540,553,607,595):
				Display_OPTION_hander.snake_change_down_HL()
			else:
				Display_OPTION_hander.snake_change_down_unHL()
			
			#on click event:
			if event.type==MOUSEBUTTONDOWN:
				if mouse_Move_In(116,13,166,110):#back to main menu
					state="main_menu"
				elif mouse_Move_In(170,250,255,350): #left arrow
					if Display_OPTION_hander.map_id == 1:
						Display_OPTION_hander.map_id=map.count
					else:
						Display_OPTION_hander.map_id=Display_OPTION_hander.map_id-1
				elif mouse_Move_In(607,253,661,358): #right arrow
					if Display_OPTION_hander.map_id == map.count:
						Display_OPTION_hander.map_id=1
					else:
						Display_OPTION_hander.map_id=Display_OPTION_hander.map_id+1
				elif mouse_Move_In(540,390,607,431):#up speed
					if Display_OPTION_hander.speed == 6:
						Display_OPTION_hander.speed = 1
					else:
						Display_OPTION_hander.speed=Display_OPTION_hander.speed+1
				elif mouse_Move_In(540,440,607,481):#down speed
					if Display_OPTION_hander.speed==1:
						Display_OPTION_hander.speed=6
					else:
						Display_OPTION_hander.speed=Display_OPTION_hander.speed-1
				elif mouse_Move_In(540,503,607,545):#snake change up
					if Display_OPTION_hander.snake_id==snake.count:
						Display_OPTION_hander.snake_id=1
					else:
						Display_OPTION_hander.snake_id=Display_OPTION_hander.snake_id+1
				elif mouse_Move_In(540,553,607,595):
					if Display_OPTION_hander.snake_id==1:
						Display_OPTION_hander.snake_id=snake.count
					else:
						Display_OPTION_hander.snake_id=Display_OPTION_hander.snake_id-1

		if state == "game":
			if event.type == KEYDOWN:
				if event.key==K_UP:
					if (Display_GAME_hander.choise_snake.prec=="down"):
						pass
					elif colision.check_eat(Display_GAME_hander.choise_snake, Display_GAME_hander.food_pos, "up"):
						Display_GAME_hander.choise_snake.eat("up")
						sound.playE()
						Display_GAME_hander.food_pos=colision.randFood(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake)
						frame_count=0
					elif colision.check(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake, "up"):
						Display_GAME_hander.choise_snake.move_up()
						sound.playMS()
						frame_count=0
					else:
						state="game_over"
				if event.key==K_DOWN:
					if (Display_GAME_hander.choise_snake.prec=="up"):
						pass
					elif colision.check_eat(Display_GAME_hander.choise_snake, Display_GAME_hander.food_pos, "down"):
						Display_GAME_hander.choise_snake.eat("down")
						sound.playE()
						Display_GAME_hander.food_pos=colision.randFood(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake)
						frame_count=0
					elif colision.check(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake, "down"):
						Display_GAME_hander.choise_snake.move_down()
						sound.playMS()
						frame_count=0
					else:
						state="game_over"
				if event.key==K_LEFT:
					if (Display_GAME_hander.choise_snake.prec=="right"):
						pass
					elif colision.check_eat(Display_GAME_hander.choise_snake, Display_GAME_hander.food_pos, "left"):
						Display_GAME_hander.choise_snake.eat("left")
						sound.playE()
						Display_GAME_hander.food_pos=colision.randFood(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake)
						frame_count=0
					elif colision.check(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake, "left"):
						Display_GAME_hander.choise_snake.move_left()
						sound.playMS()
						frame_count=0
					else:
						state="game_over"
				if event.key==K_RIGHT:
					if (Display_GAME_hander.choise_snake.prec=="left"):
						pass
					elif colision.check_eat(Display_GAME_hander.choise_snake, Display_GAME_hander.food_pos, "right"):
						Display_GAME_hander.choise_snake.eat("right")
						sound.playE()
						Display_GAME_hander.food_pos=colision.randFood(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake)
						frame_count=0
					elif colision.check(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake, "right"):
						Display_GAME_hander.choise_snake.move_right()
						sound.playMS()
						frame_count=0
					else:
						state="game_over"
				if event.key==K_p:
					state="pause"

		if state == "game_over":
			if mouse_Move_In(255,401,382,449):
				Display_GAME_hander.go_retry_HL()
			else:
				Display_GAME_hander.go_retry_unHL()
			if mouse_Move_In(420,401,546,449):
				Display_GAME_hander.go_menu_HL()
			else:
				Display_GAME_hander.go_menu_unHL()
			if mouse_Move_In(176+170,133+332, 176+289,133+380):
				Display_GAME_hander.go_save_HL()
			else:
				Display_GAME_hander.go_save_unHL()
			

			if event.type==MOUSEBUTTONDOWN:
				if mouse_Move_In(255,401,382,449):
					Display_GAME_hander.reset()
					state="game"
					if game_mode=="level":
						now_level=1
						now_score=0
						Display_OPTION_hander.level_mode(now_level)
						Display_GAME_hander=GAME_Control(Display_OPTION_hander.speed, snake.get_snake(Display_OPTION_hander.snake_id), map.getmap(Display_OPTION_hander.map_id))

				elif mouse_Move_In(420,401,546,449):
					Display_GAME_hander.reset()
					state="main_menu"

				elif mouse_Move_In(176+170,133+332, 176+289,133+380) and not Display_GAME_hander.game_over_save_Disabled:
					score.addHighScore(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed, DISPLAYSURF)

		if state == "pause":
			if event.type == KEYDOWN:
				if event.key==K_c:
					state="game"

		if state == "congratulation":
			if mouse_Move_In(255,401,382,449):
				Display_GAME_hander.c_retry_HL()
			else:
				Display_GAME_hander.c_retry_unHL()
			if mouse_Move_In(420,401,546,449):
				Display_GAME_hander.c_menu_HL()
			else:
				Display_GAME_hander.c_menu_unHL()
			if mouse_Move_In(176+170,133+332, 176+289,133+380):
				Display_GAME_hander.go_save_HL()
			else:
				Display_GAME_hander.go_save_unHL()
			

			if event.type==MOUSEBUTTONDOWN:
				if mouse_Move_In(255,401,382,449):
					Display_GAME_hander.reset()
					state="game"
					if game_mode=="level":
						now_level=1
						now_score=0
						Display_OPTION_hander.level_mode(now_level)
						Display_GAME_hander=GAME_Control(Display_OPTION_hander.speed, snake.get_snake(Display_OPTION_hander.snake_id), map.getmap(Display_OPTION_hander.map_id))

				elif mouse_Move_In(420,401,546,449):
					Display_GAME_hander.reset()
					state="main_menu"

				elif mouse_Move_In(176+170,133+332, 176+289,133+380) and not Display_GAME_hander.game_over_save_Disabled:
					score.addHighScore(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed, DISPLAYSURF)


	#use handeres to display up the windown
	if state == "main_menu":
		display_MN(Display_MAIN_MENU_hander)
		DISPLAYSURF.blit(MAIN_MENU, (0,0))
		pass
	elif state == "option":
		display_OP(Display_OPTION_hander)
		DISPLAYSURF.blit(OPTION, (0,0))
		pass
	elif state == "game":
		frame_count=frame_count+1
		if frame_count == (60/Display_GAME_hander.speed):
			frame_count=0
			if colision.check_eat(Display_GAME_hander.choise_snake, Display_GAME_hander.food_pos, Display_GAME_hander.choise_snake.prec):
				Display_GAME_hander.choise_snake.eat(Display_GAME_hander.choise_snake.prec)
				sound.playE()
				Display_GAME_hander.food_pos=colision.randFood(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake)
			elif colision.check(map.MAP_2D_MAZE, Display_GAME_hander.choise_snake, Display_GAME_hander.choise_snake.prec):
				Display_GAME_hander.choise_snake.auto_move()
				sound.playMS()
			else:
				state="game_over"
		if game_mode=="level":
			store_score=now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed
			if store_score>=level.levels[now_level]['change_score']:
				now_score=store_score
				if now_level<level.max_level:
					now_level+=1
					Display_GAME_hander.choise_snake.reset()
					Display_GAME_hander.speed=level.levels[now_level]['speed']
					Display_GAME_hander.choise_map=map.getmap(level.levels[now_level]['map'])
					map.reset_2D_maze()
					map.set_2D_maze(Display_GAME_hander.choise_map)
				elif now_level == level.max_level:
					state="congratulation"

		display_GAME(Display_GAME_hander)
		DISPLAYSURF.blit(GAME_PLAY, (0,0))
	elif state == "game_over":
		isHighScore = score.checkHighscore(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed)
		if not isHighScore:
			Display_GAME_hander.go_disable()
		display_GAME_OVER(Display_GAME_hander)
		DISPLAYSURF.blit(GAME_PLAY, (0,0))
	elif state == "pause":
		pause_img=pygame.image.load("img/surfaces/pause.png")
		DISPLAYSURF.blit(pause_img,(176,133))
	elif state == "congratulation":
		isHighScore = score.checkHighscore(now_score+(len(Display_GAME_hander.choise_snake.maze)-3)*Display_GAME_hander.speed)
		if not isHighScore:
			Display_GAME_hander.go_disable()
		display_CONGRATULATION(Display_GAME_hander)
		DISPLAYSURF.blit(GAME_PLAY, (0,0))
		pass

	pygame.display.update()
	fpsClock.tick(FPS)

