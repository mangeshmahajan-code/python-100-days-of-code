from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake =Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() >300 or snake.head.ycor() < -300 :
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[2:] :
        if snake.head.distance(segment) < 10 :
            game_is_on =False
            scoreboard.game_over()

screen.exitonclick()
