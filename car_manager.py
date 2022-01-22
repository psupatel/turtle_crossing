COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.start_x = 270
        self.start_y = 0
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.carspeed = STARTING_MOVE_DISTANCE


    def move_car(self):
        """ Moves cars forward. If car goes off screen, generates a new car """
        self.forward(self.carspeed)
        if self.xcor() < -310:
            self.generate_new_car()

    def move_faster(self):
        """ Increases car speed for the next level. """
        self.carspeed += MOVE_INCREMENT

    def generate_car(self):
        """ Creates a randomly colored car on the screen for the starting screen """
        self.color(random.choice(COLORS))
        self.start_x = random.randint(-200, 330)
        self.start_y = random.randint(-250, 250)
        self.goto(self.start_x, self.start_y)

    def generate_new_car(self):
        """ Creates a randomly colored car at the right edge, distributed vertically
        at random for ongoing gameplay """
        self.color(random.choice(COLORS))
        self.start_x = 280
        self.start_y = random.randint(-250, 250)
        self.goto(self.start_x, self.start_y)






