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

#creates variables for player position
player_x = 262.5
player_y = 375

#draws the rectabgle which the player can move
player = pygame.draw.rect(screen, red, (player_x, player_y, 75, 25))


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
                screen.blit(player, (player_x, player_y))
            #is the key being pressed yhe right arrow
            elif event.key == pygame.K_RIGHT:
                #if so move the x position to the right
                player_x += 10
                screen.blit(player, (player_x, player_y))
    #redraws the entire screen
    pygame.display.update()