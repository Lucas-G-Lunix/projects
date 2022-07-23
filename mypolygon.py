import math
import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_lenght = 2 * math.pi * r * (angle / 360)
    n = int(arc_lenght/3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n
    polyline(t, n, step_lenght, step_angle)
def circle(t, r):
    arc(t, r, 360)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)
def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)
def pie_piece(t, n)
bob = turtle.Turtle()
flower(bob, 6, 30, 90)
turtle.mainloop()
