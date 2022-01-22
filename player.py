STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_player()

    def move_player(self):
        """ Moves player forward """
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        """ Moves player to starting position """
        self.goto(STARTING_POSITION)

