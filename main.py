from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)

screen.listen()
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')

game_is_on = True
while game_is_on: 
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Detect collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # Detect when right paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()