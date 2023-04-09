from microbit import *
import music
import random


DIRECTIONS = {
    "N": {
        "image": Image.ARROW_N,
        "freq": 200,
    },
    "S": {
        "image": Image.ARROW_S,
        "freq": 250,
    },
    "W": {
        "image": Image.ARROW_W,
        "freq": 300,
    },
    "E": {
        "image": Image.ARROW_E,
        "freq": 350,
    },
}

PITCH_DURATION = 100


class Game:
    def __init__(self):
        self.sequence = Sequence()
        self.input = Input()

    def start(self):
        display.show(Image.TARGET)
        music.play(music.ENTERTAINER)
        while not (button_a.is_pressed() and button_b.is_pressed()):
            display.clear()
            sleep(350)
            display.show(Image.TARGET)
            sleep(350)

        for number in "321":
            display.show(number)
            music.play(music.BA_DING)
            sleep(1000)
        music.play(music.JUMP_UP)

    def end(self):
        display.show(Image.SAD)
        music.play(music.POWER_DOWN)
        display.scroll(len(self.sequence) - 1)
        sleep(1500)
        self.input.clear()
        self.sequence.clear()

    def check(self):
        if self.input.check(self.sequence):
            display.show(Image.HAPPY)
            music.play(music.POWER_UP)
            sleep(1500)
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


class Sequence:
    def __init__(self):
        self.sequence = []
        self.directions = [
            DIRECTIONS["N"],
            DIRECTIONS["S"],
            DIRECTIONS["W"],
            DIRECTIONS["E"],
        ]

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        return self.sequence[key]

    def show(self):
        self.sequence.append(random.choice(self.directions))

        for direction in self.sequence:
            sleep(350)
            display.show(direction["image"])
            music.pitch(direction["freq"], PITCH_DURATION)
            sleep(350)
            display.clear()

        display.show(Image("99999:99999:99999:99999:99999"))
        sleep(350)
        display.clear()

    def clear(self):
        self.sequence.clear()


class Button:
    def __init__(self, pin):
        self.pin = pin

    def is_pressed(self):
        return self.pin.read_digital() == 0


class Input:
    def __init__(self):
        self.input = []

        self.button_N = Button(pin13)
        self.button_S = Button(pin15)
        self.button_W = Button(pin12)
        self.button_E = Button(pin14)

    def read(self):
        if self.button_N.is_pressed():
            direction_pressed = DIRECTIONS["N"]
            sleep(200)

        elif self.button_S.is_pressed():
            direction_pressed = DIRECTIONS["S"]
            sleep(200)

        elif self.button_W.is_pressed():
            direction_pressed = DIRECTIONS["W"]
            sleep(200)

        elif self.button_E.is_pressed():
            direction_pressed = DIRECTIONS["E"]
            sleep(200)

        else:
            direction_pressed = None

        if direction_pressed:
            self.input.append(direction_pressed)
            display.show(direction_pressed["image"])
            music.pitch(direction_pressed["freq"], PITCH_DURATION)
            sleep(200)
            display.clear()

    def check(self, sequence):
        while len(self.input) < len(sequence):
            self.read()
            if sequence[: len(self.input)] != self.input:
                return False
        return True

    def clear(self):
        self.input.clear()


game = Game()
game.run()
