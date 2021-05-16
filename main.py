import turtle
from paddle import Paddle
from ball import Ball
from block import Block

screen = turtle.Screen()
screen.setup(600,800)
screen.bgcolor('black')
screen.title('Break Out Game')
screen.tracer(0)

paddle = Paddle()
ball = Ball()

x_list = [-230, -120, -10, 100, 210]
y_list = [280, 255, 230, 205, 180]
blocks = []

for x in x_list:
    for y in y_list:
        block = Block(x, y)
        blocks.append(block)
screen.listen()
screen.onkey(paddle.go_left, 'Left')
screen.onkey(paddle.go_right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()

    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -300:
        ball.bounce_y()
        ball.bounce_x()

    if ball.ycor() < -380:
        ball.reset()

    for block in blocks:
        if ball.distance(block) < 50:
            ball.bounce_y()
            ball.bounce_x()
            block.goto(1000,1000)
            blocks.remove(block)


screen.exitonclick()
