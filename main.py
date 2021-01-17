from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

sc = Screen()
sc.setup(600, 600)
sc.bgcolor('black')
sc.title('Snake Game')
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if (snake.head.xcor() > 280
    or  snake.head.xcor() < -300
    or  snake.head.ycor() > 300
    or  snake.head.ycor() < -280):
        game_is_on = False
        scoreboard.gameover()

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()


sc.exitonclick()