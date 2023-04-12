from microbit import *
import random
import music
import time


DISPLAY_MIN = 0
DISPLAY_MAX = 4

BRIGHTNESS_PLAYER = 5
BRIGHTNESS_DOT = 9


class Game:
    def __init__(self):
        self.player = Player()
        self.dot = Dot()
        self.score = 0

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
        display.clear()

    def end(self):
        display.show(Image.HAPPY)
        music.play(music.CHASE)
        display.scroll(self.score)
        sleep(1500)
        self.score = 0
        display.clear()

    def check_collision(self):
        if self.player.x == self.dot.x and self.player.y == self.dot.y:
            self.score += 1
            return True
        return False

    def run(self):
        self.start()
        while True:
            display.clear()
            self.player.show()
            self.dot.show()

            start = time.ticks_ms()
            now = time.ticks_ms()

            while time.ticks_diff(now, start) < 25000:
                if time.ticks_diff(now, self.dot.time_showed) > 1000:
                    self.dot.clear()
                    self.dot.update_coordinates()
                    self.dot.show()

                self.player.clear()
                self.player.update_coordinates()

                if self.check_collision():
                    music.play(music.POWER_UP)
                    self.dot.flash()
                    while self.dot.x == self.player.x and self.dot.y == self.player.y:
                        self.dot.update_coordinates()
                    self.dot.show()

                self.player.show()
                now = time.ticks_ms()
                sleep(150)

            self.end()
            self.start()


class Input:
    def __init__(self):
        self.toggle_button = pin15
        self.joystick_x = pin1
        self.joystick_y = pin2

    def get_input(self):
        if self.toggle_button.read_digital() == 0:
            x = accelerometer.get_x() + 512
            y = 512 - accelerometer.get_y()
        else:
            x = self.joystick_x.read_analog()
            y = self.joystick_y.read_analog()
        return x, y


class Player:
    def __init__(self):
        self.x = 2
        self.y = 4
        self.brightness = BRIGHTNESS_PLAYER

        self.input = Input()

    def update_coordinates(self):
        x, y = self.input.get_input()

        if x > 600:  # right
            self.x = self.x + 1 if self.x < DISPLAY_MAX else DISPLAY_MAX
        elif x < 400:  # left
            self.x = self.x - 1 if self.x > DISPLAY_MIN else DISPLAY_MIN

        if y < 400:  # down
            self.y = self.y + 1 if self.y < DISPLAY_MAX else DISPLAY_MAX
        elif y > 600:  # up
            self.y = self.y - 1 if self.y > DISPLAY_MIN else DISPLAY_MIN

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def show(self):
        display.set_pixel(self.x, self.y, self.brightness)


class Dot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.brightness = BRIGHTNESS_DOT
        self.time_showed = time.ticks_ms()

    def get_coordinates(self):
        return (self.x, self.y)

    def update_coordinates(self):
        self.x = random.randint(DISPLAY_MIN, DISPLAY_MAX)
        self.y = random.randint(DISPLAY_MIN, DISPLAY_MAX)

    def flash(self):
        self.clear()
        sleep(50)
        self.show()
        sleep(50)
        self.clear()
        sleep(200)

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def show(self):
        self.time_showed = time.ticks_ms()
        display.set_pixel(self.x, self.y, self.brightness)


game = Game()
game.run()
