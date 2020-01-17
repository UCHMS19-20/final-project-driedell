import sys
import pygame
import random

#must call before anything else for other functions to work
pygame.init()

#creates the display screen with the desired size
width, height = 600, 400
screen = pygame.display.set_mode( (width, height) )

#set-up the colors based on RGB table
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)

#creates variables for player position
player_x = 262.5
player_y = 375

#creates a class of the falling objects
class Block:
    """This class represents the falling blocks"""
    def __init__(self, x):
        """must be done first, initiallizes the ball with attributes"""
        self.y = 0
        self.x = x
        self.vel = 10
        self.alive = True
    def update(self):
        """makes the y position of the ball change (like falling)"""
        self.y += self.vel
    def show(self):
        """draws the block with predefined values"""
        pygame.draw.rect(screen, black,  (self.x, self.y, 20, 20))
    def check(self):
        """checks if the blocks has reached the bottom of the screen"""
        if self.y >height:
            self.alive = False

#creates a group to be used in organization and loops
blocks = [Block(width/2)]

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
                player_x -= 20
                # screen.blit(player, (player_x, player_y))
            #is the key being pressed yhe right arrow
            elif event.key == pygame.K_RIGHT:
                #if so move the x position to the right
                player_x +=20
                # screen.blit(player, (player_x, player_y))

        #creates probability of a block being made
        if random.randint(1,30) == 10:
            blocks.append(Block(random.randint(0,width)))

        #creates a block if there are none
        if len(blocks) < 1:
            blocks.append(Block(random.randint(0,width)))

        #makes the display screen white
        screen.fill(white)

        #draws the rectangle which the player can move
        pygame.draw.rect(screen, red, (player_x, player_y, 75, 25))
        
        #draws the falling block
        for b in blocks:
            b.update()
            b.show()
            b.check()

        #deletes a block when it reaches the bottom
        for i in range(len(blocks)-1,-1,-1):
            if blocks[i].alive == False:
                del blocks[i]

        #redraws the entire screen
        pygame.display.flip()