FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.write(f"Level: {self.level}", font = FONT)
        self.color("black")

    def level_up(self):
        """ Prints out text of next level """
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        """ Prints game over message in the middle of the screen """
        self.goto(0,0)
        self.hideturtle()
        self.penup()
        self.write("Game over", align = "center", font = FONT)
