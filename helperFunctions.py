# import pygame
import pygame as pg
import variables as var

pg.init()

# set display size
dis = pg.display.set_mode((var.dis_width, var.dis_height))

# variables for displaying "you lose"
font = pg.font.Font('freesansbold.ttf', 25)
score_font = pg.font.Font('freesansbold.ttf', 15)


# function: display message
def display_msg(msg, colour):
    final_msg = font.render(msg, True, colour, var.colours['grey'])
    msg_rect = final_msg.get_rect()
    msg_rect.center = (var.dis_width // 2, var.dis_height // 2)
    dis.blit(final_msg, msg_rect)


# function: displays score
def display_score(score):
    msg = score_font.render(f"score: {score}", True, var.colours['white'])
    dis.blit(msg, [10, 10])


# function: draws the snake
def draw_snake(snake):
    for pixel in snake:
        pg.draw.rect(dis, var.colours['snake'], (pixel[0], pixel[1], var.pixel_size, var.pixel_size))