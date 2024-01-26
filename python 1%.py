print("Hello world!")  #first python

print(3+3,56-12,23*3,99/9,5**2) #arthimetic operators

#values and class types
print(type("Hello world!"))
print(type(42/2))
print(type(22//2))
print(type("45"))
print(type(None))
print(type(True))
print(type(False))

#assignment statements
F=17
Fariin="nabad baan kaaga tagay"
print(Fariin, F)

#Expressions and statements
n=15 #assignment statement
y=13 #also assignment statement
print(n-y) #print statement

#string operations
s="foot"
b="ball"
print(s+b)

#comment waxaa waaye waxyaabaha ku qoran midabka cagaarka

#value converting
print(int("32"))
print(int(3.99999))
print(float(32))
print(float("3.14159"))
print(str(32))
print(str(3.14159))

#math module
import math
print(2 * math.pi * 7**2)

#composition =adding and combining of many building funtions
#variable name must be left side and value must be right side

#def is a keyword that indicates that this is a function definition
def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")
def repeat_lyrics():
  print_lyrics()
  print_lyrics()
repeat_lyrics()  
def sum(x,y):#parameters can take arguments in this place or the function call place
  return x+y
print(sum(10,7)) 

#for loop
for i in range(1,7):
  print("time")
for i in range(4):
  print("nasim")

#floor devision
minutes = 105
hours = minutes //60
print(hours)

#reminder for modulus
reminder = minutes % 60
print(reminder)

#relational operators are ==,!=,>,<,>=,<=
#logical operators are and, or, not

#conditional excution
x=6
if x>5:
  print("x is greator than 5")

#alternative conditional excution
if x>5:
  print("x is greator than 5")
else:
  print("x is less than 5")

#chained conditional excution
if x==5:
  print("x is equal to 5")
elif x>5:
  print("x is greator than 5")
else:
  print("x is less than 5")

#nested conditional excution
if 0<x:
  if x<10:
    print("x is a positive single digit number")

#recursion
def countdown(n):
  if n<=0:
    print("Blastoff!")
  else:
    print(n)
    countdown(n-1)
countdown(3)    

#infinite recursion is when a recursion never reaches a base case or not related to condition.

#keyboard input is used for getting input from the user
name = input("Enter your Name:")

#fruitful functions are functions that returns values
def area(radius):
  a = math.pi * radius**2
  return a
print(area(7))  

#incremental devoplement is the process of adding small amounts to a program to make it more readable and more maintainable
def distance(x1,y1,x2,y2):
  dx = x2-x1
  dy = y2-y1
  dsquared = dx**2 + dy**2
  result = math.sqrt(dsquared)
  return result
print(distance(1,2,4,6)) 

#composition 
def circle_area(xc,yc,xp,yp):
  return area(distance(xc,yc,xp,yp))
print(circle_area(0,0,3,4))  

#boolean functions
def is_divisible(x,y):
  if x%y==0:
    return True
  else:
    return False
print(is_divisible(10,5)) 


#fibonacci function
def fibonacci(n):
  if n==0:
    return 0
  if n==1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))  

#reassignment
x=4
y=5
x=3# x will become 3
print(x+y)

#updating variables
x=4
x=x+2
print(x)

#while loop
def countdown(n):
  while n > 0:
    print(n)
    n=n-1
  print("done!")
countdown(3)



#break
while True:
  line = input(">")
  if line == "done":
    break
  print(line)  
  print("done!")

#algorithms are a set of steps to solve a problem.  

#stack diagram
#refactoring
#square root
#factorial function

