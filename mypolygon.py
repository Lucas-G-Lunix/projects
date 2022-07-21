import turtle
'''
def circle(t, r):
    circumference = 2 * 3.14 * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
def arc(t, r, angle):
    arc_length = 2 * 3.14 * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
'''
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

bob = turtle.Turtle()
turtle.mainloop()
