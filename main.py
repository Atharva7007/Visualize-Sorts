import random
from sys import exit
import time
import pygame
from pygame import mixer
pygame.init()

# Define colours RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Button(object):
    button_font = pygame.font.SysFont("georgia", 20)

    def __init__(self, x, y, width, height, text) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.surface = pygame.Surface((self.width, self.height))
        self.text = self.button_font.render(text, True, BLACK)

class MainGame(object):
    def __init__(self) -> None:
        self.WIDTH, self.HEIGHT = 500, 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        self.BAR_WIDTH = 10
        self.START = 5
        self.END = 501
        self.bar_colour = RED

        self.array = list(range(self.START, self.END, self.BAR_WIDTH))
        random.shuffle(self.array)
        self.length = len(self.array)
        
        self.CLOCK = pygame.time.Clock()
        self.FPS = 100
        
        self.beep = mixer.Sound(r"beep.wav")
        return
    
    def run(self) -> None:
        self.menu()

    def menu(self):

        self.screen.fill(BLACK)

        # Bubble Sort Button
        bsort_button = Button(100, 300, 150, 40, "Bubble Sort")
        isort_button = Button(260, 300, 150, 40, "Insertion Sort")

        heading_font = pygame.font.SysFont("georgia", 40)
        heading_text = heading_font.render("Sorting Visualization Tool", True, WHITE, BLACK)

        font = pygame.font.SysFont("arial", 20)
        menu_text = font.render("Click on one of the Sorting Algorithms below to visualize them!", True, WHITE, BLACK)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(bsort_button.rect, event.pos):
                        self.bubblesort()
                        return
                    if pygame.Rect.collidepoint(isort_button.rect, event.pos):
                        self.insertionsort()
                        return
            
            # Change button color to GREEN if mouse is hovering over it        
            if pygame.Rect.collidepoint(bsort_button.rect, pygame.mouse.get_pos()):
                bsort_button.surface.fill(GREEN)
            else:
                bsort_button.surface.fill(RED)
            bsort_button.surface.blit(bsort_button.text, bsort_button.text.get_rect(center=bsort_button.surface.get_rect().center))
            
            # Change button color to GREEN if mouse is hovering over it
            if pygame.Rect.collidepoint(isort_button.rect, pygame.mouse.get_pos()):
                isort_button.surface.fill(GREEN)
            else:
                isort_button.surface.fill(RED)
            isort_button.surface.blit(isort_button.text, isort_button.text.get_rect(center=isort_button.surface.get_rect().center))
            
            self.screen.blit(heading_text, (20, 100))
            self.screen.blit(menu_text, (20, 200))
            self.screen.blit(bsort_button.surface, bsort_button.rect)
            self.screen.blit(isort_button.surface, isort_button.rect)
            pygame.display.update()

    def bubblesort(self):
        done = False

        while not done:
            # Bubblesort algorithm
            for i in range(self.length - 1):
                for j in range(self.length - i - 1):
                    
                    # Close the window if close button is pressed
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            running = False
                            exit(0)
                    # Control FPS
                    self.CLOCK.tick(self.FPS)
                    self.screen.fill(BLACK)
                    self.beep.play()

                    if self.array[j] > self.array[j + 1]:
                        self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                    # If numbers are being compared, show them by green color else red
                    for index, element in enumerate(self.array):
                        if  index == j or index == j + 1:
                            bar_colour = RED
                        else:
                            bar_colour = WHITE
                        pygame.draw.rect(self.screen, bar_colour, (index * self.BAR_WIDTH, self.HEIGHT - element, self.BAR_WIDTH, element))

                    pygame.display.update()

            self.screen.fill(BLACK)
            for index, element in enumerate(self.array):
                pygame.draw.rect(self.screen, WHITE, (index * self.BAR_WIDTH, self.HEIGHT - element, self.BAR_WIDTH, element))

            pygame.display.update()

            done = True # Sorting is complete

        time.sleep(2)
        return

    def insertionsort(self):
        done = False

        while not done:
            
            for i in range(1, self.length):
                # Insertion Sort algorithm
                key = self.array[i]
                j = i-1

                while j >= 0 and self.array[j] > key:
                    self.array[j+1] = self.array[j]
                    j -= 1
                    self.beep.play() # beep denotes a comparison
                
                    # Close the window if close button is pressed
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            running = False
                    
                    # Control FPS
                    self.CLOCK.tick(self.FPS)
                    self.screen.fill(BLACK)
                    
                    # If numbers are being compared, show them by green color else red
                    for index, element in enumerate(self.array):
                        if  index == j or element == key:
                            bar_colour = RED
                        else:
                            bar_colour = WHITE

                        # Draw a bar representing the elements of the array
                        pygame.draw.rect(self.screen, bar_colour, (index * self.BAR_WIDTH, self.HEIGHT - element, self.BAR_WIDTH, element))
                    
                    pygame.display.update()
                
                self.array[j+1] = key
            
            self.screen.fill(BLACK)
            for index, element in enumerate(self.array):
                pygame.draw.rect(self.screen, WHITE, (index * self.BAR_WIDTH, self.HEIGHT - element, self.BAR_WIDTH, element))
            pygame.display.update()

            done = True # Sorting is complete

        time.sleep(2)

if __name__ == "__main__":
    game = MainGame()
    game.run()