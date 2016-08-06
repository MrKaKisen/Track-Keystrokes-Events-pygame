#Made by Vilhelm Prytz 2016

#init pygame
import pygame
pygame.init()

#vars
display_width = 350
display_height = 75
version = 1.0

#setting upp window & pygame stuff
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tracking keystrokes")
clock = pygame.time.Clock()

#functions
def updateDisplay():    
        pygame.display.update()
        clock.tick(60)

#main code_loop
def code_loop():
        gameExit = False

        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                        else:
                                print(event)

        updateDisplay()

code_loop()
pygame.quit()
quit()
