import turtle
import math
import random
import time









SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Team Orange DosBox!")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()


#Keyboard Bindings

game_state = "splash"
#Main Game Loop
while True:

    #clear screen
    pen.clear()


    #Game Code
    if game_state == "splash":
        wn.bgpic("splash.gif")


    #Clear Screen
    wn.update()




