from microbit import *
import random

min_value = 0
max_value = 4

position_x = 4
position_y = 4
brightness_position = 5

goal_x = 0
goal_y = 0
brightness_goal = 9

display.set_pixel(position_x, position_y, brightness_position)
display.set_pixel(goal_x, goal_y, brightness_goal)


while True:    
    sleep(800)
    display.set_pixel(position_x, position_y, 0)
    
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    if x > 0:
        position_x = position_x + 1 if position_x < max_value else max_value
    elif x < 0:
        position_x = position_x - 1 if position_x > min_value else min_value
        
    if y > 0:
        position_y = position_y + 1 if position_y < max_value else max_value
    elif y < 0:
        position_y = position_y - 1 if position_y > min_value else min_value

    if position_x == goal_x and position_y == goal_y:
        display.set_pixel(goal_x, goal_y, 0)
        sleep(150)
        display.set_pixel(goal_x, goal_y, brightness_goal)
        sleep(150)
        display.set_pixel(goal_x, goal_y, 0)
        sleep(400)

        while goal_x == position_x and goal_y == position_y:
            goal_x = random.randint(min_value, max_value)
            if goal_x == 0:
                goal_y = random.randint(min_value, max_value)
            else:
                goal_y = 0
        display.set_pixel(goal_x, goal_y, brightness_goal)
    
    display.set_pixel(position_x, position_y, brightness_position)
