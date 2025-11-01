from turtle import Turtle
class Paddle(Turtle) :

    def __init__(self,x_coordinate):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(x=x_coordinate, y=0)

    def go_up(self):
            y_coordinate = self.ycor()
            x_coordinate = self.xcor()
            self.goto(x=x_coordinate, y=y_coordinate + 20)

    def go_down(self):
            y_coordinate = self.ycor()
            x_coordinate = self.xcor()
            self.goto(x=x_coordinate, y=y_coordinate - 20)
