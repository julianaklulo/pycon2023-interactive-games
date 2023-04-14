# Create interactive games using electronics and MicroPython

Repository with the game code examples for my [presentation](https://us.pycon.org/2023/schedule/presentation/142/) at PyCon US 2023.

To run it, you'll need:

* BBC micro:bit (V1 or V2)
* [Gamepad for BBC micro:bit](https://www.waveshare.com/wiki/Joystick_for_micro:bit)

If you don't have a gamepad, you can use 4 push buttons, a joystick and a buzzer.

The code will work if the GPIO pins are mapped accordingly.

## Game example #1: Genius
Genius (in Brazil) or Simon is a game where a sequence of colors is showed to the player, that must repeat it in the correct order.

For this example, the input uses 4 push buttons that represent directions.

Each direction is indicated by an arrow and a corresponding pitch sound.

If player inputs the sequence correctly, a new direction is added to the sequence.

https://user-images.githubusercontent.com/8601883/232163891-6214c188-3eea-479f-b281-99ab1437a50a.mp4

## Game example #2: Chase the Dot
In this game the player needs to catch a dot on the display, which will change the location if it's not caught in 1s.

The player can use the joystick or the accelerometer to play.

After 25s, the game ends and displays how many dots were caught.

https://user-images.githubusercontent.com/8601883/232163946-d06dbe19-c907-4063-8dab-59ccc95d7fd2.mp4

## Game example #3: Car Crash
In the Car Crash game there are obstacles coming in the direction of the car.

The player uses the joystick to move the car and avoid crashing it.

After avoiding an obstacle, the game gets faster, making it harder to play.

https://user-images.githubusercontent.com/8601883/232163996-db302895-d5da-48fe-afb2-c105743fcf76.mp4
