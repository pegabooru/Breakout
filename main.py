# Imports
import turtle as trtl
import random as rand

# Init. turtle stuff
wn = trtl.Screen()
wn.bgcolor('black')
# Add images
blocksImg = "img/green.gif"
playerImg = "img/paddle.gif"
ballImg = "img/ball.gif"
wn.addshape(blocksImg)
wn.addshape("img/yellow.gif")
wn.addshape("img/red.gif")
wn.addshape(playerImg)
wn.addshape(ballImg)

# Init global variables before start
blocks = []
blocksX = []
blocksY = []
blocksWd = 30
blocksHt = 10

# Functions
def spawnBlock(): # Spawn and initialize blocks
  block = trtl.Turtle()
  block.shape(blocksImg)
  block.penup()
  block.speed(0)
  blocks.append(block)

def paddleLeft(): # Move player left and right
  ply.goto(ply.xcor()-15,ply.ycor())
def paddleRight():
  ply.goto(ply.xcor()+15,ply.ycor())

ply = trtl.Turtle()
ply.shape(playerImg)
ply.penup()
ply.speed(0)
ply.setpos(ply.xcor(), -300)

ball = trtl.Turtle()
ball.shape(ballImg)
ball.penup()
ball.speed(0)
ball.setpos(ply.xcor(), -290)
dir = rand.randint(0,1)
if (dir == 0):
  ball.left(45)
elif (dir == 1):
  ball.right(45)

wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")

wn.listen()
wn.mainloop()
