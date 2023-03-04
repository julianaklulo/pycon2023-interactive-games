from microbit import *
import music
import random


DIRECTIONS = {
    'N': (Image.ARROW_N, 200),
    'S': (Image.ARROW_S, 250),
    'W': (Image.ARROW_W, 300),
    'E': (Image.ARROW_E, 350),
}


class Game():
    def __init__(self):
        self.sequence = Sequence()
        self.input = Input()
    
    def start(self):
        while not (button_a.is_pressed() and button_b.is_pressed()):
            display.show(Image.TARGET)
            sleep(350)
            display.clear()
            sleep(350)

        for number in ("54321"):
            display.show(number)
            sleep(1000)

    def end(self):
        display.show(Image.SAD)
        sleep(1500)
        self.input.clear()
        self.sequence.clear()

    def check(self):
        if self.input.check(self.sequence.sequence):
            display.show(Image.HAPPY)
            sleep(1000)
            display.clear()
            self.input.clear()
            return True
        return False

    def run(self):
        self.start()
        while True:
            self.sequence.show()
            correct_answer = self.check()
            if not correct_answer:
                self.end()
                self.start()


class Sequence():
    def __init__(self):
        self.sequence = []
        self.directions = [DIRECTIONS['N'], DIRECTIONS['S'], DIRECTIONS['W'], DIRECTIONS['E']]
    
    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]

    def show(self):
        self.sequence.append(random.choice(self.directions))

        for direction in self.sequence:
            sleep(500)
            display.show(direction[0])
            music.pitch(direction[1], 100)
            sleep(500)
            display.clear()
        
        display.show(Image('99999:99999:99999:99999:99999'))
        sleep(350)
        display.clear()

    def clear(self):
        self.sequence.clear()


class Button():
    def __init__(self, pin):
        self.pin = pin
        self.previous_state = False
    
    def is_pressed(self):
        return self.pin.read_digital() == 0

    def was_pressed(self):
        new_state = self.is_pressed()
        was_pressed = new_state and not self.previous_state
        self.previous_state = new_state
        return was_pressed


class Input():
    def __init__(self):
        self.input = []
        self.direction_pressed = None
        
        self.button_N = Button(pin13)
        self.button_S = Button(pin15)
        self.button_W = Button(pin12)
        self.button_E = Button(pin14)

    def read(self):
        if self.button_N.is_pressed():
            self.direction_pressed = DIRECTIONS['N']
            sleep(200)

        elif self.button_S.is_pressed():
            self.direction_pressed = DIRECTIONS['S']
            sleep(200)

        elif self.button_W.is_pressed():
            self.direction_pressed = DIRECTIONS['W']
            sleep(200)
        
        elif self.button_E.is_pressed():
            self.direction_pressed = DIRECTIONS['E']
            sleep(200)
        
        else:
            self.direction_pressed = None

        if self.direction_pressed:
            self.input.append(self.direction_pressed)
            display.show(self.direction_pressed[0])
            music.pitch(self.direction_pressed[1], 100)
            sleep(200)
            display.clear()

    def check(self, sequence):
        while len(self.input) < len(sequence):
            self.read()
            if sequence[:len(self.input)] != self.input:
                return False
        return True

    def clear(self):
        self.input.clear()

game = Game()
game.run()
