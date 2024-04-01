#!/usr/bin/env python3

import sys
import turtle

def border(t, screen_x, screen_y):
    """(Turtle, int, int)

    Draws a border around the canvas in red.
    """
    # Lift the pen and move the turtle to the center.
    t.penup()
    t.home()

    # Move to lower left corner of the screen; leaves the turtle
    # facing west.
    t.forward(screen_x / 2)
    t.right(90)
    t.forward(screen_y / 2)
    t.setheading(180)           # t.right(90) would also work.
    
    # Draw the border
    t.pencolor('blue')
    t.pensize(10)
    n = 8
    t.forward(screen_x * (n+1)/(2*n))
    t.pendown()
    for distance in (screen_x *(n-1)/(2*n), screen_y, screen_x, screen_y, screen_x *(n-1)/(2*n)):
        t.forward(distance)
        t.right(90)

    # Raise the pen and move the turtle home again; it's a good idea
    # to leave the turtle in a known state.
    t.penup()
    t.home()

def runline(t, screen_x, screen_y, backsteps, angle):
    """(Turtle, int, int, int, int)

    Draw a line in a room
    """
    lby = (-1) * screen_y * 1/2
    uby = screen_y * 1/2
    lbx = (-1) * screen_x * 1/2
    ubx = screen_x * 1/2
    print (t.xcor(), t.ycor(), lby, uby, lbx, ubx)
    t.pencolor('green')
    t.pendown()
    while t.xcor() < ubx and t.xcor() > lbx and t.ycor() < uby and t.ycor() > lby:
        #print (t.xcor(), t.ycor(), lby, uby, lbx, ubx)
        t.fd(1)
    print (t.xcor(), (1/8)*screen_x, t.xcor(), (-1/8)*screen_x)
    if t.ycor() <= lby and t.xcor() < (1/16)*screen_x and t.xcor() > (-1/16)*screen_x:
        t.fd(25)
        return False
    t.pencolor('red')
    t.bk(backsteps)
    t.right(angle)
    return True

def square(t, size, color):
    """(Turtle, int, str)

    Draw a square of the chosen colour and size.
    """
    t.pencolor(color)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)

def machet(startangle, angle):
    # Create screen and turtle.
    screen = turtle.Screen()
    screen.title('Turtle Bot Demo')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()

    # Uncomment to draw the graphics as quickly as possible.
    t.speed(0)

    # Draw a border around the canvas
    border(t, screen_x, screen_y)

    # Draw a set of nested squares, varying the color.
    # The squares are 10%, 20%, etc. of half the size of the canvas.
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    t.pensize(3)
    t.right(startangle)
    counter = 0
    while counter < 100 and runline(t, screen_x, screen_y, 20, angle):
        counter+=1

    canvas = screen.getcanvas()
    canvas.create_text(-120,-230,fill="darkblue",font="Arial 20 bold",
                        text="Startwinkel", anchor="nw")
    canvas.create_text(0,-230,fill="darkblue",font="Arial 20 bold",
                        text=str(startangle)+"°",anchor="nw")

    canvas.create_text(-120,-205,fill="darkblue",font="Arial 20 bold",
                        text="Drehwinkel",anchor="nw")
    canvas.create_text(0,-205,fill="darkblue",font="Arial 20 bold",
                        text=str(angle)+"°",anchor="nw")

    if counter == 100:
        canvas.create_text(-120,-180,fill="red",font="Arial 20 bold",
                            text="Abbruch",anchor="nw")
    else:
        canvas.create_text(-120,-180,fill="darkblue",font="Arial 20 bold",
                            text="Schritte",anchor="nw")
        canvas.create_text(0,-180,fill="darkblue",font="Arial 20 bold",
                            text=str(counter),anchor="nw")

    canvas.postscript(file="c:/temp/turtlebot-"+ str(counter) + "." + str(angle) + "(" + str(startangle)+").eps")
    canvas.delete("all")

def main():
    starters = [90, 100, 130, 156, 180, 200, 245, 280, 300, 320, 12, 40, 45]
    angles = [55, 90, 94, 120, 170, 20, 50]
    for starter in starters:
        for angle in angles:
            machet (starter, angle)

main()