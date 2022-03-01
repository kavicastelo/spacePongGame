#!/usr/bin/env python3
import turtle
import time

#create screen
screen = turtle.Screen()
screen.title('PONG GAME')
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.bgpic('bg.png')

#border
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(-450, 240)
turtle.pendown()
turtle.color('red')
turtle.forward(900)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(900)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

#score
score = 0
delay = 0.1

#pad
pad = turtle.Turtle()
pad.speed(0)
turtle.addshape('spaceShip.gif')
pad.shape('spaceShip.gif')
pad.shapesize(1, 4)
pad.color('red')
pad.penup()
pad.goto(0, -200)
pad.direction = 'stop'

#ball
ball = turtle.Turtle()
ball.speed(0)
turtle.addshape('fireBall.gif')
ball.shape('fireBall.gif')
ball.color('red')
ball.penup()
ball.goto(130, 30)
ball.forward(100)
ball.right(135)
ball.direction = 'stop'

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 250)
scoring.write("Score:", align="center", font=("Courier", 24, "bold"))

#name
name = turtle.Turtle()
name.speed(0)
name.color('white')
name.penup()
name.hideturtle()
name.goto(0, -250)
name.write("Developed by: Kavi Castelo", align="center", font=("Courier", 14, "italic"))

#instructions
ins = turtle.Turtle()
ins.speed(0)
ins.color('white')
ins.penup()
ins.hideturtle()
ins.goto(0, -280)
ins.write("Press 'r' to RESET and Press 'q' to EXIT..", font=("Courier", 11, "italic"))

#how to move
def pad_go_right():
    if pad.direction != "left":
        pad.direction = "right"

def pad_go_left():
    if pad.direction != "right":
        pad.direction = "left"

def system_exit():
    turtle.bye()

def reset():
    ball.setx(130)
    ball.sety(30)
    ball.direction = 'stop'
    scoring.clear()

def pad_move():
    if pad.direction == "right":
        x = pad.xcor()
        pad.setx(x + 30)
        pad.direction = 'stop'

    if pad.direction == "left":
        x = pad.xcor()
        pad.setx(x - 30)
        pad.direction = 'stop'

    if pad.xcor() > 420 or pad.xcor() < -420:
        x = pad.xcor()
        y = pad.ycor()
        pad.setx(x)
        pad.sety(y)

def move_ball(ball):
    ball.begin_fill()
    ball.end_fill()


#keybord bindings
screen.listen()
screen.onkeypress(pad_go_right, "Right")
screen.onkeypress(pad_go_left, "Left")
screen.onkeypress(system_exit, "q")
screen.onkeypress(reset, "r")
pad_move()

#main loop
while True:
    try:
        ball.clear()
        move_ball(ball)
        screen.update()
        ball.forward(15)
    except Exception as e:
        quit()

    #border spin
    if ball.xcor() > 440 or ball.xcor() < -440 or ball.ycor() > 230 or ball.ycor() < -250:
        ball.back(0)
        ball.right(90)

    # hit the ball on pad
        screen.update()
    if ball.ycor() < -200:
        if pad.distance(ball) < 40:
            ball.forward(1)
            ball.right(90)
            ball.back(0)
            ball.right(150)

            scoring.clear()
            score += 1
            scoring.write("Score:{}".format(score), align="center", font=("Courier", 24, "bold"))
            delay -= 0.001

    #end game
    try:
        if ball.ycor() < -248 or pad.xcor() > 450 or pad.xcor() < -450:
            time.sleep(1)
            screen.clear()
            screen.bgpic('gameOver.png')
            screen.bgcolor('black')
            scoring.goto(0, 0)
            scoring.write("   GAME OVER \n Your Score is: {}".format(score),
                          align='center', font=("Courier", 30, "bold"))
            ins.write("   Press 'q' to exit the game..", font=("Courier", 18, ""))
            screen.onkeypress(system_exit, "q")
    except Exception as e:
        quit()

    pad_move()
    time.sleep(0.1)
    turtle.Terminator()
