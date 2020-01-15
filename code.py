import sys
import pygame
import random

#must call before anything else for other functions to work
pygame.init()

#creates the display screen with the desired size
screen = pygame.display.set_mode( (600, 400) )

#set-up the colors based on RGB table
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)

#creates variables for player position
player_x = 262.5
player_y = 375

#creates a class of the falling objects
class Block(pygame.sprite.Sprite)
    """This class represents the falling balls
    it is derived from the Sprite class which is preloaded"""
    def __init__(self, color, width, height, x, y):
        """must be done first, initiallizes the ball with attributes"""
        #This calls the Sprite parent class
        super().__init__()
        self.image = pygame.Surface(width, height)
        self.image.fill(color)
        self.rect =self.image.get_rect()
        self.rect.y = random.randrange(0,400)
        self.rect.x = random.randrange(0,600)
    def update(self):
        """makes the y position of the ball change (like falling)"""
        self.rect.y +=random.randrange(1,5)



# Main loop, game goes inside this loop
while True:
    # do something for each event in the event queue
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()
        #checks to see if current event is a key being pressed
        elif event.type == pygame.KEYDOWN:
            #is the key being pressed the left arrow?
            if event.key == pygame.K_LEFT:
                #if so move the x positon to the left
                player_x -= 10
                # screen.blit(player, (player_x, player_y))
            #is the key being pressed yhe right arrow
            elif event.key == pygame.K_RIGHT:
                #if so move the x position to the right
                player_x += 10
                # screen.blit(player, (player_x, player_y))

        #makes the display screen white
        screen.fill(white)
        pygame.display.flip()

        #draws the rectangle which the player can move
        pygame.draw.rect(screen, red, (player_x, player_y, 75, 25))
        
        #draws the falling block

        #redraws the entire screen
        pygame.display.update()