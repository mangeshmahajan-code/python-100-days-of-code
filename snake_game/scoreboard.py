from turtle import Turtle
ALIGN = "center"
FRONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,265)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard (self):
        self.write(f"Score : {self.score}",align=ALIGN,font=FRONT)

    def game_over (self):
        self.goto(0,0)
        self.write("Game over.",align=ALIGN,font=FRONT)

    def increase_score (self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
