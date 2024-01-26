import turtle as t
t.speed(8)
t.hideturtle()

#simple repitition
"""
for i in range(4):
    t.fd(100)
    t.lt(90)
    """
#encapsulation
"""
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(t) 
"""

#Generalization
"""
def square(length , angle):
    for i in range(4):
        t.fd(length)
        t.lt(angle)
square(100,90)   
"""

#interface design
import math
def circle(t,r):
    circumference = 2*math.pi*r
    r=7
    n= 50
    length =circumference/n
    circle(t,n,length)
t.mainloop()
