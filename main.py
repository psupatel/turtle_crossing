# import required python libraries
import time
from turtle import Screen

# import classes from local python files
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# create screen object and display screen. Put 'exitonclick' at end of code
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the turtle, scoreboard, and car objects
# car creation calls the CarManager class 30 times to create a list of objects
# calls to CarManager class will use a for loop to iterate through that list
player = Player()
score = Scoreboard()
cars = []

for i in range(20):
    cars.append(CarManager())

for i in cars:
    i.generate_car()

# record screen input.  If the player clicks up arrow, move them forward
screen.listen()
screen.onkey(key="Up", fun=player.move_player)

# game logic
game_is_on = True

while game_is_on:

    time.sleep(0.1)

    # move the cars
    for i in cars:
        i.move_car()

    # if the turtle gets to the top screen, advance level and difficulty
    if player.ycor() > 280:
        player.reset_player()
        score.level_up()
        for i in cars:
            i.move_faster()

    # if the turtle gets hit by a car, end the game
    for i in cars:
        if player.distance(i) < 20:
            score.game_over()
            game_is_on = False
    screen.update()

screen.exitonclick()

