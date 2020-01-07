import sys
import pygame

pygame.init()

screen = pygame.display.set_mode( (600, 400) )

white = pygame.Color(255,255,255)

screen.fill(white)
pygame.display.flip()

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
