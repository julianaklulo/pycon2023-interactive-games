from microbit import *
import random
import music


DISPLAY_MIN = 0
DISPLAY_MAX = 4


class Game:
    def __init__(self):
        self.player = Player()
        self.dot = Dot()
        self.playing = False

    def start(self):
        display.show(Image.TARGET)
        music.play(music.ENTERTAINER)
        while not (button_a.is_pressed() and button_b.is_pressed()):
            display.clear()
            sleep(350)
            display.show(Image.TARGET)
            sleep(350)

        for number in ("321"):
            display.show(number)
            music.play(music.BA_DING)
            sleep(1000)
    
        music.play(music.JUMP_UP)
        self.playing = True

    def check_pause(self):
        if button_a.was_pressed():
            self.playing = False
            sleep(150)
        if button_b.was_pressed():
            self.playing = True
            sleep(150)
    
    def check_collision(self):
        if self.player.x == self.dot.x and self.player.y == self.dot.y:
            return True
        return False

    def run(self):
        self.start()
        display.clear()
        self.player.draw()
        self.dot.draw()
        
        while True:
            self.check_pause()
            if self.playing:
                sleep(200)
                self.player.clear()
                self.player.update_coordinates()
                if self.check_collision():
                    music.play(music.POWER_UP)
                    self.dot.flash()
                    while self.dot.x == self.player.x and self.dot.y == self.player.y:
                        self.dot.update_coordinates()
                    self.dot.draw()
                self.player.draw()
    

class Player:
    def __init__(self):
        self.x = 2
        self.y = 4
        self.brightness = 5
        self.button = pin15
        self.mode = "accelerometer"

    def set_mode(self):
        if self.button.read_digital() == 0:
            self.mode = "joystick"
        else:
            self.mode = "accelerometer"
    
    def update_coordinates(self):
        self.set_mode()
        if self.mode == "accelerometer":
            accel_x = accelerometer.get_x()
            accel_y = accelerometer.get_y()
    
            if accel_x > 0:
                self.x = self.x + 1 if self.x < DISPLAY_MAX else DISPLAY_MAX
            elif accel_x < 0:
                self.x = self.x - 1 if self.x > DISPLAY_MIN else DISPLAY_MIN
            
            if accel_y > 0:
                self.y = self.y + 1 if self.y < DISPLAY_MAX else DISPLAY_MAX
            elif accel_y < 0:
                self.y = self.y - 1 if self.y > DISPLAY_MIN else DISPLAY_MIN

        elif self.mode == "joystick":
            joystick_x = pin1.read_analog()
            joystick_y = pin2.read_analog()

            if joystick_x > 600:
                self.x = self.x + 1 if self.x < DISPLAY_MAX else DISPLAY_MAX
            elif joystick_x < 400:
                self.x = self.x - 1 if self.x > DISPLAY_MIN else DISPLAY_MIN
                
            if joystick_y < 400:
                self.y = self.y + 1 if self.y < DISPLAY_MAX else DISPLAY_MAX
            elif joystick_y > 600:
                self.y = self.y - 1 if self.y > DISPLAY_MIN else DISPLAY_MIN

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def draw(self):
        display.set_pixel(self.x, self.y, self.brightness)


class Dot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.brightness = 9

    def get_coordinates(self):
        return (self.x, self.y)

    def update_coordinates(self):
        self.x = random.randint(DISPLAY_MIN, DISPLAY_MAX)
        self.y = random.randint(DISPLAY_MIN, DISPLAY_MAX)
        
    def flash(self):
        self.clear()
        sleep(150)
        self.draw()
        sleep(150)
        self.clear()
        sleep(400)

    def clear(self):
        display.set_pixel(self.x, self.y, 0)

    def draw(self):
        display.set_pixel(self.x, self.y, self.brightness)
