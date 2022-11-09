from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_counter()

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance <= 9:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
