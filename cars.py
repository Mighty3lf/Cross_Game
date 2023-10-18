from turtle import Turtle, colormode
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

class CarManager:
    def __init__(self):
        self.all_cars = []
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random_color())
            y = random.randint(-230,230)
            new_car.goto(300, y)
            self.all_cars.append(new_car)
        
    def move(self):
        for i in range(len(self.all_cars)):
            new_x = self.all_cars[i].xcor() - 10
            self.all_cars[i].goto(new_x, self.all_cars[i].ycor())