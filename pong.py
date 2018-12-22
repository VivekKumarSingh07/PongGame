import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width = 800, height= 600)
window.tracer(0)

#Score
score_a = 0
score_b = 0

# Player A bat
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Player B bat
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = -0.05

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(" Player A:0 PlayerB:0", align="center", font=("Courier", 24, "normal"))

# Functions to move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyword Interrupt 
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#Main Loop for game
while True:
    window.update()

    # To move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # To Check the border condition
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")


    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(" Player A:{} PlayerB:{}".format(score_a , score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(" Player A:{} PlayerB:{}".format(score_a , score_b), align="center", font=("Courier", 24, "normal"))
    
    # Collisions
    if (ball.xcor() > 340 and ball.xcor()<350)  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350)  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")