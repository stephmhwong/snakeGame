# This is a simple game of snake

# import packages/ files
import pygame as pg
import random
import helperFunctions as hf
import variables as var

# init pygame
pg.init()

pg.display.update()

clock = pg.time.Clock()


# function: play game
def play_game():
    # bools to determine end of game
    game_over = False
    end_game = False
    start_game = False
    snake_speed = 10

    # while user wants to play again
    while not end_game:

        # variables for position of snake
        x_pos = 299
        y_pos = 199
        x_change = 0
        y_change = 0

        # create snake object
        snake = [[x_pos, y_pos]]
        snake_size = 1

        # rand generate initial food position
        food_x = round(random.randrange(9, var.dis_width - 11, var.pixel_size))
        food_y = round(random.randrange(9, var.dis_height - 11, var.pixel_size))

        # draw snake initial position
        hf.draw_snake(snake)
        pg.display.update()  # update display

        while not game_over:

            # check for keyboard inputs/ mouseclick input
            for event in pg.event.get():
                # close window, end game
                if event.type == pg.QUIT:
                    end_game = True
                    game_over = True
                # for keyboard press
                if event.type == pg.KEYDOWN:
                    start_game = True
                    if event.key == pg.K_LEFT:
                        x_change = -var.pixel_size
                        y_change = 0
                    if event.key == pg.K_RIGHT:
                        x_change = var.pixel_size
                        y_change = 0
                    if event.key == pg.K_DOWN:
                        x_change = 0
                        y_change = var.pixel_size
                    if event.key == pg.K_UP:
                        x_change = 0
                        y_change = -var.pixel_size

            # change position of rectangle
            x_pos += x_change
            y_pos += y_change

            # error checking cannot go over itself (the snake)
            if start_game and [x_pos, y_pos] in snake:
                game_over = True

            # draw snake and food
            hf.dis.fill(var.colours['background'])
            pg.draw.rect(hf.dis, var.colours['food'], (food_x, food_y, var.pixel_size, var.pixel_size))  # food

            # if no food eaten move the snake by adding pixel and deleting a pixel
            snake.append([x_pos, y_pos])
            if len(snake) > snake_size:
                del snake[0]

            hf.draw_snake(snake)
            hf.display_score(snake_size - 1)
            pg.display.update()  # update display

            # error checking in bounds
            if x_pos + 10 > var.dis_width or x_pos < 0 or y_pos + 10 > var.dis_height or y_pos < 0:
                game_over = True

            # check if food found and generate new food (step 10)
            if x_pos == food_x and y_pos == food_y:
                food_x = round(random.randrange(9, var.dis_width - 11, var.pixel_size))
                food_y = round(random.randrange(9, var.dis_height - 11, var.pixel_size))
                snake_size += 1

                # change snake speed
                if snake_size % 5 == 0:
                    snake_speed += 2

            clock.tick(snake_speed)

        # restart game/ start game
        while game_over and not end_game:
            hf.display_msg('GAME OVER.... x - exit, return - play again', var.colours['gameover'])
            pg.display.update()

            # wait for user keyboard input
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end_game = True
                    game_over = False
                if event.type == pg.KEYDOWN:
                    # exit the game press key 'x'
                    if event.key == pg.K_x:
                        end_game = True
                        game_over = False
                    # play again press return key
                    if event.key == pg.K_RETURN:
                        game_over = False
                        end_game = False
                        start_game = False
                        snake_speed = 10

    pg.display.update()  # update display
    pg.quit()


# run the game
play_game()
