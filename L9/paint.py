import os

import pygame
import sys
from pygame.locals import *

windowSurface = pygame.display.set_mode((480, 320))

# Colors list
GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
PRETTY_BLUE = (0, 238, 195)

eraser = pygame.image.load("img/eraser.png")
eraser = pygame.transform.scale(eraser, (40, 40))
eraser_rect = pygame.Rect(27, 210, 40, 40)

pygame.init()

# font setup
menu_font = pygame.font.SysFont('Arial', 17)
menu_text = menu_font.render("My Paint", True, BLACK)

clear_text = menu_font.render("Clear", True, BLACK)
brush_text = menu_font.render("Brushes", True, BLACK)

save_text = menu_font.render("SAVE", True, BLACK)

draw = False
brush_size = 5
brush_color = GREEN

menu_rect = pygame.Rect(0, 0, 100, 320)
screen_rect = pygame.Rect(100, 0, 380, 320)

green_rect = pygame.Rect(5, 55, 20, 20)
red_rect = pygame.Rect(27, 55, 20, 20)
blue_rect = pygame.Rect(49, 55, 20, 20)
pink_rect = pygame.Rect(71, 55, 20, 20)
light_blue_rect = pygame.Rect(5, 77, 20, 20)
yellow_rect = pygame.Rect(27, 77, 20, 20)
orange_rect = pygame.Rect(49, 77, 20, 20)
purple_rect = pygame.Rect(71, 77, 20, 20)
dark_green_rect = pygame.Rect(5, 99, 20, 20)
brown_rect = pygame.Rect(27, 99, 20, 20)
black_rect = pygame.Rect(49, 99, 20, 20)
pretty_blue_rect = pygame.Rect(71, 99, 20, 20)

clear_rect = pygame.Rect(10, 290, 70, 25)

thin_brush = pygame.Rect(5, 185, 20, 20)
medium_brush = pygame.Rect(27, 185, 20, 20)
thick_brush = pygame.Rect(49, 185, 20, 20)
supa_brush = pygame.Rect(71, 185, 20, 20)

save_rect = pygame.Rect(5, 260, 90, 25)
save_flag = False
file_number = 1
pygame.draw.rect(windowSurface, WHITE, screen_rect)


def save_image():
    TODO()


def draw_brushes():
    if brush_size == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, thin_brush, brush_border)
    pygame.draw.circle(windowSurface, BLACK, thin_brush.center, 1)
    pygame.draw.rect(windowSurface, BLACK, thin_brush, brush_border)

    if brush_size == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, medium_brush, brush_border)
    pygame.draw.circle(windowSurface, BLACK, medium_brush.center, 3)
    pygame.draw.rect(windowSurface, BLACK, medium_brush, brush_border)

    if brush_size == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, thick_brush, 1)
    pygame.draw.circle(windowSurface, BLACK, thick_brush.center, 5)
    pygame.draw.rect(windowSurface, BLACK, thick_brush, brush_border)

    if brush_size == 10:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(windowSurface, BLACK, supa_brush, brush_border)
    pygame.draw.circle(windowSurface, BLACK, supa_brush.center, 10)
    pygame.draw.rect(windowSurface, BLACK, supa_brush, brush_border)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False

    # Drawing dot when mousebuttondown
    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[0] > 100:
        pygame.draw.circle(windowSurface, brush_color, mouse_pos, brush_size)
        save_flag = False

    # collision detection for COLOR
    if draw:
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
        if light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
        if black_rect.collidepoint(mouse_pos):
            brush_color = BLACK
        if brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
        if pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = PRETTY_BLUE

    # collision detection for eraser
    if draw:
        if eraser_rect.collidepoint(mouse_pos):
            brush_color = WHITE

    # collision detection for CLEAR
    if draw:
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(windowSurface, WHITE, screen_rect)

    pygame.draw.rect(windowSurface, GRAY, menu_rect)
    windowSurface.blit(menu_text, (10, 20))

    pygame.draw.line(windowSurface, BLACK, (0, 40), (100, 40))
    pygame.draw.line(windowSurface, BLACK, (0, 45), (100, 45))

    pygame.draw.rect(windowSurface, DARK_GRAY, clear_rect)
    windowSurface.blit(clear_text, (17, 290))

    windowSurface.blit(brush_text, (10, 160))
    pygame.draw.line(windowSurface, BLACK, (0, 180), (100, 180))

    # Blit the save rect
    pygame.draw.rect(windowSurface, DARK_GRAY, save_rect)
    windowSurface.blit(save_text, (13, 262))

    # Collision detection for SAVE
    if draw == True and save_flag == False:
        if save_rect.collidepoint(mouse_pos):
            save_image()

    # collision detectin for BRUSH SIZE
    if draw:
        if thin_brush.collidepoint(mouse_pos):
            brush_size = 1
        if medium_brush.collidepoint(mouse_pos):
            brush_size = 3
        if thick_brush.collidepoint(mouse_pos):
            brush_size = 5
        if supa_brush.collidepoint(mouse_pos):
            brush_size = 10

    # rect for brush_color
    pygame.draw.rect(windowSurface, GREEN, green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, green_rect, border)

    pygame.draw.rect(windowSurface, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, red_rect, border)

    pygame.draw.rect(windowSurface, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, blue_rect, border)

    pygame.draw.rect(windowSurface, PINK, pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, pink_rect, border)

    pygame.draw.rect(windowSurface, LIGHT_BLUE, light_blue_rect)
    if brush_color == LIGHT_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, light_blue_rect, border)

    pygame.draw.rect(windowSurface, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, yellow_rect, border)

    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)

    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)

    pygame.draw.rect(windowSurface, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, dark_green_rect, border)

    pygame.draw.rect(windowSurface, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, purple_rect, border)

    pygame.draw.rect(windowSurface, BLACK, black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, WHITE, black_rect, border)

    pygame.draw.rect(windowSurface, BROWN, brown_rect)
    if brush_color == BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, brown_rect, border)

    pygame.draw.rect(windowSurface, PRETTY_BLUE, pretty_blue_rect)
    if brush_color == PRETTY_BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, pretty_blue_rect, border)

    # RECT FOR ERASER
    windowSurface.blit(eraser, eraser_rect)
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, eraser_rect, border)

    # Rect for brush size
    draw_brushes()

    pygame.display.update()
