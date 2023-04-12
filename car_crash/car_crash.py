from microbit import *
import random
import music

LEFT_BORDER = 1
RIGHT_BORDER = 3

BRIGHTNESS_BORDER = 5
BRIGHTNESS_PLAYER = 7
BRIGHTNESS_OBSTACLE = 9

MAX_REFRESH_RATE = 8
MIN_REFRESH_RATE = 1


class Game:
    def __init__(self):
        self.player = Player()
        self.obstacle = Obstacle()
        self.border = Border()
        self.screen = Screen()
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
        display.show(Image.SAD)
        music.play(music.POWER_DOWN)
        display.scroll(self.score)
        sleep(1500)
        self.score = 0
        self.obstacle.reset()
        self.player.reset()
        self.screen.reset()

    def check_collision(self):
        return self.player.x == self.obstacle.x and self.player.y == self.obstacle.y

    def run(self):
        self.start()
        
        iteration = 0
        while True:
            self.player.update_coordinates()            
            self.screen.update_buffer(self.border, self.player, self.obstacle)
            self.screen.show()
            iteration += 1

            if iteration >= self.screen.refresh:
                if self.obstacle.y == 4: # hit bottom
                    if self.check_collision():
                        self.end()
                        self.start()
                        continue
                    music.pitch(300, 100, wait=False)
                    self.score += 1
                    self.screen.speedup()
                self.border.move()                
                self.obstacle.update_coordinates()
                iteration = 0
            
            sleep(100)
            
            

class Player:
    def __init__(self):
        self.x = 2
        self.y = 4
        self.brightness = BRIGHTNESS_PLAYER
        self.joystick_x = pin1

    def update_coordinates(self):
        x = self.joystick_x.read_analog()
        
        if x < 400: # left
            if self.x > LEFT_BORDER:
                self.x -= 1        
        elif x > 600: # right
            if self.x < RIGHT_BORDER:
                self.x += 1
    
    def reset(self):
        self.x = 2
        self.y = 4


class Obstacle:
    def __init__(self):
        self.x = 2
        self.y = 0
        self.brightness = BRIGHTNESS_OBSTACLE
        
    def update_coordinates(self):
        if self.y < 5:
            self.y += 1
        if self.y == 5:
            self.x = random.randint(LEFT_BORDER, RIGHT_BORDER)
            self.y = 0

    def reset(self):
        self.x = 2
        self.y = 0


class Border:
    def __init__(self):
        self.top = 1
        self.bottom = 2
        self.brightness = BRIGHTNESS_BORDER

    def move(self):
        self.bottom = self.bottom + 1 if self.bottom < 4 else 0
        self.top = self.bottom + 1 if self.top < 4 else 0


class Screen:
    def __init__(self):
        self.buffer = "00000:00000:00000:00000:00000"
        self.refresh = MAX_REFRESH_RATE
        
    def update_buffer(self, border, player, obstacle):
        border_space = ["0", "0", "0", "0", "0"]
        border_space[border.top] = str(border.brightness)
        border_space[border.bottom] = str(border.brightness)

        obstacle_space = ["0", "0", "0"]
        obstacle_space[obstacle.x - 1] = str(obstacle.brightness)

        buffer = ["00000", "00000", "00000", "00000", "00000"]
        
        for row in range(5):
            buffer[row] = border_space[row] + "000" + border_space[row]

        buffer[obstacle.y] = (
            buffer[obstacle.y][0] + "".join(obstacle_space) + buffer[obstacle.y][4]
        )
      
        buffer[player.y] = (
            buffer[player.y][: player.x]
            + str(player.brightness)
            + buffer[player.y][player.x + 1 :]
        )

        self.buffer = ":".join(buffer)

    def show(self):
        display.show(Image(self.buffer))

    def reset(self):
        self.refresh = MAX_REFRESH_RATE

    def speedup(self):
        if self.refresh >= MIN_REFRESH_RATE:
            self.refresh -= 1

game = Game()
game.run()