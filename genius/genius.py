from microbit import *
import random

sequence = []
input = []

def start_game():
    while not (button_a.is_pressed() and button_b.is_pressed()):
        display.show(Image.DIAMOND)
        sleep(350)
        display.clear()
        sleep(350)

    for number in ("54321"):
        display.show(number)
        sleep(1000)


def show_sequence():
    directions = [Image.ARROW_E, Image.ARROW_W]
    sequence.append(random.choice(directions))

    for direction in sequence:
        sleep(500)
        display.show(direction)
        sleep(500)
        display.clear()
    
    display.show(Image('55555:'
                       '55555:'
                       '55555:'
                       '55555:'
                       '55555'))
    sleep(350)
    display.clear()
    
    

def read_input():
    direction_pressed = None
    
    while len(input) < len(sequence):
        if button_a.is_pressed():
            direction_pressed = Image.ARROW_W
            sleep(100)

        elif button_b.is_pressed():
            direction_pressed = Image.ARROW_E
            sleep(100)

        if direction_pressed:
            display.show(direction_pressed)
            sleep(250)
            display.clear()
            
            index = len(input)
            input.append(direction_pressed)
            if sequence[index] != direction_pressed:
                break
            direction_pressed = None
        

def show_game_over():
    display.show(Image.SAD)
    sleep(1500)
    sequence.clear()
    input.clear()


def show_correct_answer():
    display.show(Image.HAPPY)
    sleep(1500)
    input.clear()


start_game()

while True:
    show_sequence()
    read_input()
    if input != sequence:
        show_game_over()
        start_game()
    else:
        show_correct_answer()
