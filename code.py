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

#creates the player as a rect, has attributes to be used later
player_rect = pygame.Rect(player_x, player_y, 50, 50)

#creates a class of the falling objects
class Block:
    """This class represents the falling blocks"""
    def __init__(self, x):
        """must be done first, initiallizes the ball with attributes"""
        self.rect = pygame.Rect(x, 0, 20, 20)
        self.vel = 10
        self.alive = True
    def update(self):
        """makes the y position of the ball change (like falling)"""
        self.rect.y += self.vel
    def show(self):
        """draws the block with predefined values"""
        pygame.draw.rect(screen, black, self.rect)
    def check(self):
        """checks if the blocks has reached the bottom of the screen"""
        if self.rect.y >height:
            self.alive = False
    def check_hit(self, other):
        """check if the falling block hits the player using rect properties"""       
        if self.rect.colliderect(other):
            sys.exit()

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
                player_rect.x -= 30
                # screen.blit(player, (player_x, player_y))
            #is the key being pressed yhe right arrow
            elif event.key == pygame.K_RIGHT:
                #if so move the x position to the right
                player_rect.x += 30
                # screen.blit(player, (player_x, player_y))

    #creates probability of a block being made, and will add to list
    if random.randint(1,20) == 10:
        blocks.append(Block(random.randint(0,width)))

    #creates a block if there are none
    elif len(blocks) < 6:
        blocks.append(Block(random.randint(0,width)))

    #makes the display screen white
    screen.fill(white)

    #draws the rectangle which the player can move
    player = pygame.draw.rect(screen, red, player_rect)
    
    #draws the falling block by calling predefined functions
    for b in blocks:
        b.update()
        b.show()
        b.check()
        b.check_hit(player)

    #deletes a block when it reaches the bottom
    for i in range(len(blocks)-1,-1,-1):
        if blocks[i].alive == False:
            del blocks[i]

    #redraws the entire screen
    pygame.display.flip()