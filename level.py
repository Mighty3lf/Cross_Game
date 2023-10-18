from turtle import Turtle

FONT = ("Courier", 15, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.goto(0, 240)
        self.write(f"Nível: {self.level}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Nível: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("magenta")
        self.write("GAME OVER", align="center", font=("Courier", 35, "normal"))