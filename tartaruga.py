from turtle import Turtle

STARTING_POSITION = (0,- 240)

class Tartaruga(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    
    def left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())
    
    def right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())
    
    def restart_position(self):
        self.goto(STARTING_POSITION)