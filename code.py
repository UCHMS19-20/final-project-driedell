import sys
import pygame

#must call before anything else for other functions to work
pygame.init()

#creates the display screen with the desired size
screen = pygame.display.set_mode( (600, 400) )

#set-up the colors based on RGB table
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)

#makes the display screen white
screen.fill(white)
pygame.display.flip()

#draws the rectabgle which the player can move
player = pygame.draw.rect(screen, red, (262.5, 375, 75, 25))

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
    pygame.display.update()