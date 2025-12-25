from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score= Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect the collision with the upper wall .
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()

    # Detect the collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325 :
        ball.bounce_x()

    #  Detect R paddle misses
    if ball.xcor() >380 :
        ball.rest_position()
        score.r_point()

    #  Detect L paddle misses
    if ball.xcor() < -380 :
        ball.rest_position()
        score.l_point()

screen.exitonclick()
