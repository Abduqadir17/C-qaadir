#QUESTION 5-1

import datetime

x = datetime.datetime.now()
print(x)


#QUESTION 5-2
a,b,c=4,3,5
n=2
if a**n+b**n==c**n:
    print("right")
else:
    print("wrong")    





    
#QUESTION 5-3
a,b,c=9,16,25

if a + b > c and a + c > b and b + c > a:
        
        print("Yes, you can form a triangle.")
else:
        print("No, you cannot form a triangle.")

#QUESTION 5-4
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

#QUESTION 5-5
import turtle as t
def draw(t, length, n):
     if n == 0:
          return
     angle = 50
     t.fd(length*n)
     t.lt(angle)
     draw(t, 200, n-1)
     t.rt(2*angle)
     draw(t, 200, n-1)
     t.lt(angle)
     t.bk(length*n)

#QUESTION 5-6
import turtle as t


def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = t.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

t.mainloop()     
    




