### Task 1

You have to add drawings to the almost finished game `TicTacToe`. The functionality of the game works without drawings, but we need to see it in reality!

You are given the file `tictactoe.py` which contains the source code of the project with explanations for each of the functions.

Your goal is to write code for the 2 functions that need drawings:

- `draw_grid()` - Creates a board with 3 lines on the x and y axes
- `draw_markers()` - marks `X` and `O` on the board.

**_draw_grid()_**

- Color constants can be used in color fields!
- The background, the color of the grid (3x3 lines) must be visible and easily distinguishable on the board (not the same color!).
- You can use `lines` for the grid (Check the screen height and width)

**_draw_markers()_**

- Use a multidimensional array `markers` that contains a matrix version of tictactoe. Where 1 is `X` and -1 is `O`.
- To draw `X`, use 2 lines (85/15)
- To draw `O`, use a circle (50/50)

NOTE: Add `line_width` for each figure. If you want, you can customize it.

### Task 2

### Task 3

### Task 4

### Task 5

Your goal is to write a "Car race" game in python using pygame library.

You are given 5 cars images and soundtrack to the game in the `data` folder.

Create a `Car` class in `Car.py` file:

- img_name - name of the car's image (path)
- scale - height and width of the car's image
- pos - initial position coordinates of the car
- img - scaled car's image

```python
import pygame
import random

class Car:

	def __init__(self, img_name, scale, pos):
        self.img_name = img_name
        self.scale = scale
        self.pos = pos
        self.img = self.set_scale()

	# load and scale the image
	def set_scale(self):
		...

	# change position of the car
	def random_walk(self):
		...
```

Import `Car` class into the main file.

Before writing the game itself set the initial parameters of the game:

- Ask the user's guess (number of the car) on what car will win
- Set the soundtrack to the game `music.wav` from the `data` folder
- Set display's height as `800` and width as `600`
- Set caption to `Cars Race`
- Create 5 car objects using their names and add them into the `cars` list

```python
car_names = ['data/green_car', 'data/red_car', 'data/yellow_car', 'data/purple_car', 'data/orange_car']

cars = []
init_pos_weight = 50
for car_name in car_names:
    car = Car(car_name, (100, 50), [100, init_pos_weight])
    cars.append(car)
    init_pos_weight += 100
```

The beginning of the game should look like this:
![](data/screenshot.jpg?raw=true)

In the screen you have to draw the finish line and all cars should race by random walk (by using `random_walk` from `Car` class). The first car that will get to the finish - a winner. If the user guessed the winner car correctly print `YOU WON!`, `YOU LOST!` otherwise.

NOTE: Use `pygame` and `random` packages.

### Task 6

### Task 7

### Task 8

### Task 9

### Task 10

### Task 11

Create simple Mario game. Inside forlder `mario`, you can find images for this task.  
Mario can walk and jump. He can do as many jumps as he wants, however he can walk and stay only on bricks.  
Game ends if Mario takes coin or falls down.  
Try to use `running.png` and `stay.png` for this task.  
Good Luck, use your creativity! ☻

### Task 12

### Task 13

### Task 14
