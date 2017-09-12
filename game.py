# 1. Include pygame
# 	Include pygame which we got from pip:
import pygame
# From the math module (built into python), get the fabs module (absolute value)
from math import fabs
import random
#pygame.mixer.pre_init(44100, 16, 2, 4096) # For background music
# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()
# Background music
# ouch = pygame.mixer.Sound('goblin_sounds/ouch.wav')
# eat = pygame.mixer.Sound('goblin_sounds/eat.wav')
pygame.mixer.music.load('goblin_sounds/happy.mp3') # Background music
# pygame.mixer.music.set_volume(0.5) # Medium volume (goes up to 1)


# 3. Create a screen with a particular size
screen_width = 600
screen_height = 800
screen_size = (screen_width, screen_height)

# Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)

# Set a pointless caption
pygame.display.set_caption("Goblin Chase")



# Set up a var with our image
background_image = pygame.image.load('goblin_images/leg_hair.jpg')
hero_image = pygame.image.load('goblin_images/fred.png')
goblin_image = pygame.image.load('goblin_images/flea.png')
monster_image = pygame.image.load('goblin_images/tick.png')
enemy_image = pygame.image.load('goblin_images/gene.jpg')





img_dim = 40 # Size of icons

# Dictionaries!
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0,
	"status": ""
}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 15
}

monster = {
	"x": 250,
	"y": 250,
	"speed": 1
}

enemy = {
	"x": 100,
	"y": 100,
	"speed": 1
}

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

# def game_over():
# 	hero["status"] = "YOU LOST!!"


# counter = 0
# 4. Create a game loop (while)
# Create a boolean for whether the game should be going on
game_on = True
pygame.mixer.music.play(-1) # Loop it
while game_on:
	# We are inside the main game loop.
	# It will keep running as long as our bool is true
	# Note ctrl-c will kill python (if needed)

# 5. Add a quit event (Python needs an escape)
# Pygame comes with an event loop! (sort of like JS)
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
		# The user clicked the red x in the top left
			game_on = False # Gets out of while loop!
		elif event.type == pygame.KEYDOWN: # Any key is pushed.
			# print "User pressed a key!"
			# if ((screen_height - img_dim) > hero['y'] > 0 and (screen_width - img_dim) > hero['x'] > 0):
			if event.key == keys["up"]:
				# User pressed up!
				# hero['y'] -= hero['speed']
				keys_down['up'] = True
			elif event.key == keys["down"]:
				# hero['y'] += hero['speed']
				keys_down['down'] = True
			elif event.key == keys["right"]:
				# hero['x'] += hero['speed']
				keys_down['right'] = True
			elif event.key == keys["left"]:
				# hero['x'] -= hero['speed']
				keys_down['left'] = True
			# else:
			# 	if (screen_height < hero['y']):
			# 		hero['y'] -= img_dim
			# 	elif (0 > hero['y']):
			# 		hero['y'] += img_dim
			# 	elif (screen_width < hero['x']):
			# 		hero['x'] -= img_dim
			# 	elif (0 > hero['x']):
			# 		hero['x'] += img_dim

		elif event.type == pygame.KEYUP:
			if event.key == keys['up']:
				# The user let go of the key. See if that matters.
				keys_down['up'] = False
			if event.key == keys['down']:
				keys_down['down'] = False
			if event.key == keys['right']:
				keys_down['right'] = False
			if event.key == keys['left']:
				keys_down['left'] = False


	if keys_down['up']:
		hero['y'] -= hero['speed']
	elif keys_down['down']:
		hero['y'] += hero['speed']
	if keys_down['right']:
		hero['x'] += hero['speed']
	elif keys_down['left']:
		hero['x'] -= hero['speed']

	# Random monster movement
	for i in range (0, random.randint(1, 4) * 500):
		move_var = random.randint(1, 4)
		if (i % 3 == 0):
			if (move_var == 1):
				monster['x'] += monster["speed"]
				monster['y'] += monster["speed"]
				# if (monster['x'] > screen_width - img_dim): # If he hits the sides
				# 	move_var = 2
				# elif (monster['y'] > screen_width - img_dim):
				# 	move_var = 3
			elif (move_var == 2):
				monster['x'] -= monster["speed"]
				monster['y'] += monster["speed"]
				# if (monster['x'] < 0):
				# 	move_var = 1
				# elif (monster['y'] > screen_width - img_dim):
				# 	move_var = 4
			elif (move_var == 3):
				monster['x'] += monster["speed"]
				monster['y'] -= monster["speed"]
				# if (monster['x'] > screen_width - img_dim):
				# 	move_var = 4
				# elif (monster['y'] < 0):
				# 	move_var = 1
			elif (move_var == 4):
				monster['x'] -= monster["speed"]
				monster['y'] -= monster["speed"]
				# if (monster['x'] < 0):
				# 	move_var = 3
				# elif (monster['y'] < 0):
				# 	move_var = 2


	


		#	if (monster["x"] > screen_width - img_dim):
		 # 		monster["x"] -= monster["speed"]
		 # 	if (monster["x"] < 0):
			# 	monster["x"] += monster["speed"]
			# if (monster["y"] > screen_height - img_dim):
			# 	monster["y"] -= monster["speed"]
			# if (monster["y"] < 0):
			# 	monster["y"] += monster["speed"]
	# 	print counter
	# 	counter += 1
	# counter = 0
		# if (monster["x"] < screen_width - img_dim):
		# 	if (monster["y"] < screen_height - img_dim):
		# 		monster["x"] += monster["speed"]
		# 		monster["y"] += monster["speed"]
		# 	else:
		# 		monster["y"] -= monster["speed"]
		# else:
		# 	monster["x"] -= monster["speed"]
	# monst_move = True
	# while monst_move:
	
		# if (counter < random.randint(1, 4) * 60):
		# # monst_x = random.randint(1, 2)
		# # if monst_x == 1:
		#  	monster["x"] += monster["speed"]
		# # elif monst_x == 2:
		# # 	monster["x"] -= monster["speed"]
		# # monst_y = random.randint(1, 2)
		# # if monst_y == 1:
		#  	monster["y"] += monster["speed"]
		# # elif monst_y == 2:
		# # 	monster["y"] -= monster["speed"]
		# # if (monster["x"] > screen_width - img_dim):
		# # 	monster["x"] -= monster["speed"]
		# # if (monster["x"] < 0):
		# # 	monster["x"] += monster["speed"]
		# # if (monster["y"] > screen_height - img_dim):
		# # 	monster["y"] -= monster["speed"]
		# # if (monster["y"] < 0):
		# # 	monster["y"] += monster["speed"]
		# 	monst_move = False
	#	if (counter < random.randint(1, 4) * 30):
	# 	monster["x"] += random.randint(0, monster["speed"])
	# 	monster["y"] += random.randint(0, monster["speed"])
		 # 	if (monster["x"] > screen_width - img_dim):
		 # 		monster["x"] -= monster["speed"]
		 # 	if (monster["x"] < 0):
			# 	monster["x"] += monster["speed"]
			# if (monster["y"] > screen_height - img_dim):
			# 	monster["y"] -= monster["speed"]
			# if (monster["y"] < 0):
			# 	monster["y"] += monster["speed"]
	# else:
	# 	counter = 0
	#	monst_move = False
	# COLLISION DETECTION
	distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	if (distance_between < img_dim): # Goal
		hero["wins"] += 1
		hero["speed"] += 1.2
		monster["speed"] += .1
		pygame.mixer.Sound.play(pygame.mixer.Sound('goblin_sounds/oh_yeah.wav'))
		if (hero["wins"] > 4):
			enemy["speed"] += 1
		goblin['x'] = random.randint(0, screen_width - img_dim)
		goblin['y'] = random.randint(0, screen_height - img_dim)
	# If "monster" gets us...
	distance_between = fabs(hero['x'] - monster['x']) + fabs(hero['y'] - monster['y'])
	if (distance_between < img_dim):
		hero["status"] = "YOU LOST!!"
		pygame.mixer.Sound.play(pygame.mixer.Sound('goblin_sounds/eat.wav'))
	# If "enemy" gets us...
	distance_between = fabs(hero['x'] - enemy['x']) + fabs(hero['y'] - enemy['y'])
	if (distance_between < img_dim and hero["wins"] > 3):
		# pygame.mixer.music.stop()
		pygame.mixer.Sound.play(pygame.mixer.Sound('goblin_sounds/ouch.wav'))
		hero["status"] = "YOU LOST!!"
		# game_on = False
		# print "YOU LOSE!!!"
	# Borders! Continues across to opposite side of screen.
	if (hero['y'] > screen_height - img_dim):
		hero['y'] = 0
		# keys_down['down'] = False
	elif (hero['y'] < 0):
		hero['y'] = screen_height - img_dim
		# keys_down['up'] = False
	if (hero['x'] > screen_width - img_dim):
		hero['x'] = 0
		# keys_down['right'] = False
	elif (hero['x'] < 0):
		hero['x'] = screen_width - img_dim

	if (monster['y'] > screen_height - img_dim):
		monster['y'] = 0
		# keys_down['down'] = False
	elif (monster['y'] < 0):
		monster['y'] = screen_height - img_dim
		# keys_down['up'] = False
	if (monster['x'] > screen_width - img_dim):
		monster['x'] = 0
		# keys_down['right'] = False
	elif (monster['x'] < 0):
		monster['x'] = screen_width - img_dim
		# keys_down['left'] = False

	# else:
	#	print "not touching"

# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit (block image transfer) takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you want to draw it?
	pygame_screen.blit(background_image, [0, 0])

	# Make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero["wins"]), True, (0, 0, 0))
	pygame_screen.blit(wins_text, [40, 40])
	font2 = pygame.font.Font(None, 72)
	lose_text = font2.render("%s" % (hero["status"]), True, (0, 0, 0))
	pygame_screen.blit(lose_text, [110, 100])
	

	pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]])
	pygame_screen.blit(monster_image, [monster["x"], monster["y"]])

	# Enemy chases us!
	# This is down here so the "enemy" image shows up over the background.
	if (hero["wins"] > 3):
		pygame_screen.blit(enemy_image, [enemy["x"], enemy["y"]])
		if enemy["x"] < hero["x"]:
			enemy["x"] += enemy["speed"]
		else:
			enemy["x"] -= enemy["speed"]
		if enemy["y"] < hero["y"]:
			enemy["y"] += enemy["speed"]
		else:
			enemy["y"] -= enemy["speed"]
	
	


# 7. Repeat 6 over and over...
	pygame.display.flip()
	# counter += 1
	# if (counter % 30 == 0):
	# 	print counter