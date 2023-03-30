import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()



#game variables
screen_width = 300
screen_height = 300
line_width = 2

markers = [] 
clicked = False 
pos = []  
player = 1  

winner = 0
game_over = False

count = 0


RED = (255,0,0) 
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#define font
font = pygame.font.SysFont(None, 40)

#Create play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2 + 50, 160, 30)



# Screen creation
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')


'''
Game board creation.
'''
def draw_grid():
    # TODO
    pass


'''
#Markers creation 
'''
def create_markers():
    for x in range(3):
        row = [0]*3
        markers.append(row)


'''
#Markers drawing
'''
def draw_markers():
    # TODO
    pass


'''
Checking for winner
'''
def check_winner():

    global winner
    global game_over

    y_pos = 0
    for x in markers:
        #check rows
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        #check columns
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    
    #check diagonals
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True


'''
Drawing the winner
'''
def draw_winner(winner):
    win_text = "Player " + str(winner) + " wins!"
    win_img = font.render(win_text, True, WHITE)
    pygame.draw.rect(screen, BLUE, (screen_width // 2 - 100, screen_height // 2 - 20, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 -10))

    again_text = "Play again"
    again_img = font.render(again_text, True, WHITE)
    pygame.draw.rect(screen, BLUE, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 50))    


'''
Drawing the Draw Match feedback
'''
def draw_no_winner():
    draw_text = "Match is Draw!"
    draw_img = font.render(draw_text, True, WHITE)
    pygame.draw.rect(screen, BLUE, (screen_width // 2 - 100, screen_height // 2 - 20, 200, 50))
    screen.blit(draw_img, (screen_width // 2 - 100, screen_height // 2 -10))

    again_text = "Play again"
    again_img = font.render(again_text, True, WHITE)
    pygame.draw.rect(screen, BLUE, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 50))  



# Game Loop
create_markers()

#print(markers) 

run = True
while run:

    draw_grid() #first thing to do
    draw_markers() 

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == False and count < 9:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos() #returns (x,y) of the mouse
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 100][cell_y // 100] == 0:
                    markers[cell_x // 100][cell_y // 100] = player
                    player *= -1
                    count += 1
                    check_winner()

    if game_over == True and winner != 0:
        draw_winner(winner)
    elif count == 9:
        draw_no_winner()


    #check for mouseclick to see if user has clicked on Play Again
    if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
        clicked = True
    if event.type == pygame.MOUSEBUTTONUP and clicked == True:
        clicked = False
        pos = pygame.mouse.get_pos() #returns (x,y)
        if again_rect.collidepoint(pos):
            #Reset variables
            markers = [] 
            pos = []  
            player = 1  
            winner = 0
            game_over = False
            count = 0
            create_markers()





    pygame.display.update()



pygame.quit()