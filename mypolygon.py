from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def square(t,length):
    for i in range(4):
        fd(t, length)
        lt(t)

def call_sq(q,l):
    square(q,l)

def polygon1(t,length,n):
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/n)

def polygon(t,length,n,cir):
    for i in range(n):
        fd(t, length)
        lt(t, 360.0/cir)

def circle(t,r):
    pi = 3.1415926
    circumference = 2 * pi * r
    n = int(round(circumference / 3.0))
    length = circumference / n
    polygon(t,length,n)

def arc(t,r,angle):
    pi = 3.1415926
    circumference = 2 * pi * r
    cir = int(round(circumference / 3.0))
    length = circumference / cir
    n = int(round(cir / 360.0 * angle))
    polygon(t,length,n,cir)

#circle(bob, 80)
#call_sq(bob,10)
arc(bob,80,110)
wait_for_user()
