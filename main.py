from turtle import Turtle, Screen, colormode
from tartaruga import Tartaruga
from cars import CarManager
from level import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.screensize(500,500)
screen.title("Crossing Game")
screen.tracer(0)
tartaruga = Tartaruga()
screen.colormode(255)

screen.listen()
screen.onkey(tartaruga.up, "Up")
screen.onkey(tartaruga.left, "Left")
screen.onkey(tartaruga.right, "Right")

car = CarManager()
level = Scoreboard()
speed = 0.2


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)
    car.create_car()
    car.move()
    if tartaruga.ycor() > 250:
        level.level += 1
        level.update_scoreboard()
        tartaruga.restart_position()
        if speed > 0.001 and speed > 0.041:
            speed -= 0.04
    for each in car.all_cars:
        if tartaruga.distance(each) < 20:
            game_is_on = False
            level.game_over()



screen.exitonclick()