from turtle import *
speed(1)
hideturtle()
width(4)
def rel_pos(x, y):
  penup()
  goto(pos()+(x, y))
  pendown()
def drawRoof():
  width(8)
  begin_fill()
  fillcolor("orange")
  seth(180)
  forward(200)
  seth(-120)
  forward(100)
  seth(0)
  forward(200)
  end_fill()
  seth(60)
  forward(100)
  seth(-60)
  forward(100)
  width(4)
  seth(180)
  forward(100)
def drawWalls():
  seth(-90)
  forward(120)
  seth(180)
  forward(200) 
  seth(90)
  forward(120)
  seth(0)
  forward(300)
  seth(-90)
  forward(120) 
  seth(180)
  forward(100)
def drawDoor():
  color("#004080")
  forward(80)
  begin_fill()
  fillcolor("green")
  seth(90)
  forward(80)
  seth(180)
  forward(40)
  seth(-90)
  forward(80)
  end_fill()
  rel_pos(25,40)
  width(4)
  circle(5)
def drawWindows():
  begin_fill()
  color("#004080")
  fillcolor("#336699")
  seth(-90)
  width(5)
  forward(15)
  seth(180)
  forward(30)
  seth(90)
  forward(30)
  seth(0)
  forward(30)
  seth(-90)
  forward(15)
  end_fill()
  width(2)
  seth(180)
  forward(30)
  backward(15)
  seth(90)
  forward(15)
  backward(30)
def drawHouse():
  drawRoof()
  drawWalls()
  drawDoor()
  rel_pos(-50,0)
  drawWindows()
  rel_pos(135,15)
  drawWindows()
  rel_pos(105,25)
  drawWindows()
  rel_pos(-250,250)
  done()
drawHouse()  
  
