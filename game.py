# 1. Include pygame
# 	Include pygame which we got from pip:
import pygame
# From the math module (built into python), get the fabs module (absolute value)
from math import fabs
# 2. Init pygame
# in order to use pygame, we have to run the init method
pygame.init()

# 3. Create a screen with a particular size
screen_size = (512,480)

# Actually tell pygame to set the screen up and store it
pygame_screen = pygame.display.set_mode(screen_size)

# Set a pointless caption
pygame.display.set_caption("Goblin Chase")

# Set up a var with our image
background_image = pygame.image.load('goblin_images/background.png')
hero_image = pygame.image.load('goblin_images/hero.png')
goblin_image = pygame.image.load('goblin_images/goblin.png')


# Dictionaries!
hero = {
	"x": 100,
	"y": 100,
	"speed": 20,
	"wins": 0
}

goblin = {
	"x": 200,
	"y": 200,
	"speed": 15
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

# 4. Create a game loop (while)
# Create a boolean for whether the game should be going on
game_on = True
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

	# COLLISION DETECTION
	# distance_between = fabs(hero['x'] - goblin['x']) + fabs(hero['y'] - goblin['y'])
	# if (distance_between < 32):
	# 	print "collision!"
	# else:
	# 	print "not touching"

# 6. Fill in the screen with a color (or image)
	# ACTUALLY RENDER SOMETHING
	# blit (block image transfer) takes 2 arguments...
	# 1. What do you want to draw?
	# 2. Where do you want to draw it?
	pygame_screen.blit(background_image, [0, 0])

	# Make a font so we can write on the screen
	font = pygame.font.Font(None, 25)
	wins_text = font.render("Wins: %d" % (hero["wins"]), True, (0, 0, 0))
	pygame_screen.blit(wins_text, [40,40])

	pygame_screen.blit(hero_image, [hero["x"], hero["y"]])
	pygame_screen.blit(goblin_image, [goblin["x"], goblin["y"]])


# 7. Repeat 6 over and over...
	pygame.display.flip()