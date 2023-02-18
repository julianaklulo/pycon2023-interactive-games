from microbit import *
import random

min_value = 0
max_value = 4

player_x = 2
player_y = 2

dot_x = 0
dot_y = 0

brightness_player = 5
brightness_dot = 9

playing = False


def start_game():
    global playing

    playing = False
    
    display.set_pixel(player_x, player_y, 0)
    display.set_pixel(dot_x, dot_y, 0)
    
    while not (button_a.is_pressed() and button_b.is_pressed()):
        display.show(Image.DIAMOND)
        sleep(350)
        display.clear()
        sleep(350)

    display.set_pixel(player_x, player_y, brightness_player)
    display.set_pixel(dot_x, dot_y, brightness_dot)
    
    playing = True


def update_player_coordinates():
    global player_x
    global player_y
    
    accel_x = accelerometer.get_x()
    accel_y = accelerometer.get_y()

    if accel_x > 0:
        player_x = player_x + 1 if player_x < max_value else max_value
    elif accel_x < 0:
        player_x = player_x - 1 if player_x > min_value else min_value
        
    if accel_y > 0:
        player_y = player_y + 1 if player_y < max_value else max_value
    elif accel_y < 0:
        player_y = player_y - 1 if player_y > min_value else min_value


def update_dot_coordinates():
    global dot_x
    global dot_y
    
    while dot_x == player_x and dot_y == player_y:
        dot_x = random.randint(min_value, max_value)
        if dot_x == 0:
            dot_y = random.randint(min_value, max_value)
        else:
           dot_y = 0


def flash_dot():
    display.set_pixel(dot_x, dot_y, 0)
    sleep(150)
    display.set_pixel(dot_x, dot_y, brightness_dot)
    sleep(150)
    display.set_pixel(dot_x, dot_y, 0)
    sleep(400)


start_game()
while True:
    if button_a.was_pressed():
        playing = False
        sleep(150)

    if button_b.was_pressed():
        playing = True
        sleep(150)

    if button_a.is_pressed() and button_b.is_pressed():
        display.set_pixel(dot_x, dot_y, 0)
        display.set_pixel(player_x, player_y, 0)
        sleep(200)
        start_game()
        
    if playing:
        sleep(200)        
        display.set_pixel(player_x, player_y, 0)
        
        update_player_coordinates()
        
        if player_x == dot_x and player_y == dot_y:
            flash_dot()
            update_dot_coordinates()
            display.set_pixel(dot_x, dot_y, brightness_dot)

        display.set_pixel(player_x, player_y, brightness_player)
