#CJ Patel
#Task15 - compulsory_task.py
#------------------------------------------------------------#
#import libraries
import pygame
import random

#initialise screen
pygame.init()
screen_height = 720
screen_width = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Task15 - Game")

#fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 128, 0))

#Display text
font = pygame.font.Font(None, 36)
text = font.render("Obtain the fruit, but Avoid the Monsters", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

#game characters
player = pygame.image.load("player.jpg")
monster1 = pygame.image.load("monster1.jpg")
monster2 = pygame.image.load("monster2.jpg")
monster3 = pygame.image.load("monster3.jpg")
prize = pygame.image.load("prize.jpg")

#*****************************************************************#
##height and width of images
#player_height = pygame.get_height()
#player_width = pygame.get_width()

#monster1_height = pygame.get_height()
#monster1_width = pygame.get_width()

#monster2_height = pygame.get_height()
#monster2_width = pygame.get_width()

#monster3_height = pygame.get_height()
#monster3_width = pygame.get_width()

#prize_height = pygame.get_height()
#prize_width = pygame.get_width()
#*****************************************************************#

#positions
playerXPosition = 100
playerYPosition = 300

monster1XPosition = 300
monster1YPosition = 75

monster2XPosition = 500
monster2YPosition = 550

monster3XPosition = 700
monster3YPosition = 75

prizeXPosition = 900
prizeYPosition = random.randint(50, screen_height)

#keys
keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#Loop game code
while 1:

	#blit everything to the screen
	screen.blit(background, (0, 0))

	screen.blit(player, (playerXPosition, playerYPosition))
	screen.blit(monster1, (monster1XPosition,monster1YPosition))
	screen.blit(monster2, (monster2XPosition,monster2YPosition))
	screen.blit(monster3, (monster3XPosition,monster3YPosition))
	screen.blit(prize, (prizeXPosition, prizeYPosition))

	pygame.display.flip()
	
	#loop for events in game
	for event in pygame.event.get():
    	#event to exit game
		if (event.type == pygame.QUIT):
			pygame.quit()
			exit(0)

		#key pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				keyUp = True
			if event.key == pygame.K_DOWN:
				keyDown = True
			if event.key == pygame.K_LEFT:
				keyLeft = True
			if event.key == pygame.K_RIGHT:
				keyRight = True

		#key not pressed
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_UP:
			keyUp = False
		if event.key == pygame.K_DOWN:
			keyDown = False
		if event.key == pygame.K_LEFT:
			keyLeft = False
		if event.key == pygame.K_RIGHT:
			keyRight = False
	
	#player movements
	if keyUp == True:
		if playerYPosition > 0:
			playerYPosition -= 1
	if keyDown == True:
		if playerYPosition < screen_height-100:
			playerYPosition += 1
	if keyLeft == True:
		if playerXPosition > 0:
			playerXPosition -= 1
	if keyRight == True:
		if playerXPosition < screen_width-100:
			playerXPosition += 1

	#bounding box for player
	playerBox = pygame.Rect(player.get_rect())
	playerBox.top = playerYPosition
	playerBox.left = playerXPosition

	#bounding box for monster1
	monster1Box = pygame.Rect(monster1.get_rect())
	monster1Box.top = monster1YPosition
	monster1Box.left = monster1XPosition

	#bounding box for monster2
	monster2Box = pygame.Rect(monster2.get_rect())
	monster2Box.top = monster2YPosition
	monster2Box.left = monster2XPosition

	#bounding box for monster3
	monster3Box = pygame.Rect(monster3.get_rect())
	monster3Box.top = monster3YPosition
	monster3Box.left = monster3XPosition

	#bounding box for prize
	prizeBox = pygame.Rect(prize.get_rect())
	prizeBox.top = prizeYPosition
	prizeBox.left = prizeXPosition

	#collistion of playerBox with any monsterBox
	if playerBox.colliderect(monster1Box) or playerBox.colliderect(monster2Box) or playerBox.colliderect(monster3Box):
		print("You Lose!")
		pygame.quit()
		exit(0)
	
	#collistion of playerBox with prizeBox
	if playerBox.colliderect(prizeBox):
		print("You Win!")
		pygame.quit()
		exit(0)

	monster1YPosition = monster1YPosition + 0.25
	monster2YPosition = monster2YPosition - 0.25
	monster3YPosition = monster3YPosition + 0.25

	pygame.display.flip()
