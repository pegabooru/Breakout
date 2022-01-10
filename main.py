# Imports
import turtle as trtl
import random as rand

# Init. turtle stuff
wn = trtl.Screen()
wn.bgcolor('black')
# Add images
blocksImg = "img/green.gif"
playerImg = "img/paddle.gif"
wn.addshape(blocksImg)
wn.addshape("img/yellow.gif")
wn.addshape("img/red.gif")
wn.addshape(playerImg)

# Init global variables before start
blocks = []
blocksX = []
blocksY = []
blocksWd = 30
blocksHt = 10

def spawnBlock():
  block = trtl.Turtle()
  block.shape(blocksImg)
  block.penup()
  block.speed(0)
  blocks.append(block)

def paddleLeft():
  ply.setpos(ply.xcor()-10,ply.ycor())
def paddleRight():
  ply.setpos(ply.xcor()+10,ply.ycor())

ply = trtl.Turtle()
ply.shape(playerImg)
ply.penup()
ply.speed(0)
ply.setpos(ply.xcor(), -300)

wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")

wn.listen()
wn.mainloop()
