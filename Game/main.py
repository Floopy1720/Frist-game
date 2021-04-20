import pygame

#Inzilize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

#Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480

def playerdraw(x,y):
	screen.blit(playerImg, (x,y))
	pass

#Game loop
running = True
while running:
	screen.fill((0,0,0)) 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			print("left")
			playerX += -1

		if event.key == pygame.K_RIGHT:
			print("right")
			playerX += 1

		if event.key == pygame.K_UP:
			print("up")
			playerY += -1

		if event.key == pygame.K_DOWN:
			print("down")
			playerY += 1
		

		if playerX <= 0:
			playerX = 0
		elif playerX >= 736:
			playerX = 736
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
			print("relese")
		

	playerdraw(playerX,playerY)
	pygame.display.update()