import pygame
import random
from pygame import mixer

pygame.init()

# Create an array consiting of values from 5 to 500 with a step of 20
array = list(range(5, 501, 20))
random.shuffle(array)
n = len(array)

# beep sound
beep = mixer.Sound(r"beep.wav")

# Set width and height of pygame window
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True

# Define colours RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

colour = RED

clock = pygame.time.Clock()
FPS = 10 # Frames per second
done = False

while running:
	# Close the window if close button is pressed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.exit()
			running = False

	if not done:
		# Bubblesort algorithm
		for i in range(n - 1):
			for j in range(n - i - 1):
				
				# Close the window if close button is pressed
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.exit()
						running = False
				# Control FPS
				clock.tick(FPS)
				screen.fill(BLACK)
				beep.play()

				if array[j] > array[j + 1]:
					array[j], array[j + 1] = array[j + 1], array[j]

				# If numbers are being compared, show them by green color else red
				for index, element in enumerate(array):
					if  index == j or index == j + 1:
						colour = GREEN
					else:
						colour = RED
					pygame.draw.rect(screen, colour, (index * 20, HEIGHT - element, 20, element))

				pygame.display.update()
		done = True # Sorting is complete