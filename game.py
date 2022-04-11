#MAKING A PING PONG GAME

import turtle
import winsound

#make a window for our game
wn = turtle.Screen()
wn.title("Pong made by VikrantjASWAL")
wn.bgcolor("purple")
wn.setup(width=900 , height=600)
#to run game smoother
wn.tracer(0)

#Score
score_a= 0 
score_b= 0

#paddleA
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5 ,stretch_len=1) #here size of padlle is estimated as its default size is 2px and 
                                                   #strechwid is 5*2=10
paddle_a.penup() 
paddle_a.goto(-400,0)                                                                   

#paddleB
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5 ,stretch_len=1) #here size of padlle is estimated as its default size is 2px and 
                                                   #strechwid is 5*2=10
paddle_b.penup() 
paddle_b.goto(400,0) 

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0,0)
#saperate the ball movements in x and y coordinate movements
ball.dx=0.1
ball.dy=0.1

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))



#Function of A up
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

#function of A down
def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)



#function of B up
def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
#function of B down
def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


#keyboard listen
wn.listen()
wn.onkeypress(paddle_a_up , "w")
wn.onkeypress(paddle_a_down , "s")
wn.onkeypress(paddle_b_up , "t")
wn.onkeypress(paddle_b_down , "g")


#main game loop
while   True :
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #up and down Border control
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  #Bouncing sound of ball

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy*=-1
       winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    #LEft and right border control
    if ball.xcor() > 440:
        ball.goto(0,0)
        ball.dx*=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        

    if ball.xcor() < -440:
        ball.goto(0,0)
        ball.dx*=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


     # Paddle and ball collisions
    if (ball.xcor() > 390 and ball.xcor() < 400) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(390)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        


    if (ball.xcor() < -390 and ball.xcor() > -400) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-390)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    