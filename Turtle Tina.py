# 1. import the turtle
# import pygame
import turtle

# 2. Setup the screen
turtle.setup(700,400)
wn=turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tina!")

# 3. name the turtle
tina = turtle.Turtle()
tina.shape('turtle')
tina.color('green')


# 4. Create movement
tina.penup()
tina.begin_fill()
tina.color('green')
tina.goto(30,-150)
tina.pendown()
tina.circle(130)
tina.penup()
tina.end_fill()
tina.color('white')
tina.goto(0,0)
tina.begin_fill()
tina.pendown()
tina.circle(20)
tina.penup()
tina.end_fill()
tina.begin_fill()
tina.color('black')
tina.pendown()
tina.circle(10)
tina.penup()
tina.end_fill()
tina.forward(60)
tina.right(45)
tina.begin_fill()
tina.color('white')
tina.pendown()
tina.circle(30)
tina.penup()
tina.end_fill()
tina.begin_fill()
tina.color('black')
tina.pendown()
tina.circle(10)
tina.penup()
tina.end_fill()
tina.right(90)
tina.forward(90)
tina.begin_fill()
tina.color('maroon')
tina.pendown()
tina.circle(40)
tina.penup()
tina.end_fill()
tina.goto(25,-25)





