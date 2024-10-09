import turtle
import random
import time
segment=[]
grass= turtle.Screen()
grass.bgpic("grass.gif")
grass.setup(600,600)
grass.addshape("headdown.gif")
grass.addshape("headleft.gif")
grass.addshape("headright.gif")
grass.addshape("headfront.gif")
grass.addshape("body.gif")

snake= turtle.Turtle()
snake.penup()
snake.goto(0,0)
snake.speed(5)
snake.setheading(90)
snake.shape("headfront.gif")

food = turtle.Turtle()
food.penup()
food.speed(100)
food.color("red")
food.shape("circle")
food.goto(100,10)

pen =turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(500)
pen.goto(0,250)
pen.write("Score : 0",font=("Courier",27,"bold"))

def move():
    snake.forward(3)

def up():
    if snake.heading()!=270:
        snake.setheading(90)
        snake.shape("headfront.gif")
def down():
    if snake.heading()!=90:
        snake.setheading(270)
        snake.shape("headdown.gif")
def left():
    if snake.heading()!=0:
        snake.setheading(180)
        snake.shape("headleft.gif")
def right():
    if snake.heading()!=180:
        snake.setheading(0)
        snake.shape("headright.gif")

turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()
score=0
while True:

    grass.update()
    if snake.xcor()>290 or snake.xcor()< -290 or snake.ycor()>290 or snake.ycor()< -290:
        grass.bgpic("gameover.gif")
        food.hideturtle()
    for i in segment:
        if i.distance(snake)<10:
            grass.bgpic("gameover.gif")
            food.hideturtle()

    if snake.distance(food)<20:
    
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.setpos(x,y)
        score= score+1
        pen.clear()
        pen.write("score: {}".format(score),font=("Courier",27,"bold"))
        body= turtle.Turtle()
        body.penup()
        body.speed(1)
        body.shape("body.gif")
        segment.append(body)

    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y= segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)
        
    move()


turtle.done()
