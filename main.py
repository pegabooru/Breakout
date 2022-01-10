# Imports
import turtle as trtl
import random as rand

# Init. turtle stuff
wn = trtl.Screen()

# Init global variables before start
blocks = []
blocksX = []
blocksY = []
blocksWd = 30
blocksHt = 10
blocksImg = "img/green.png"

def spawnBlock():
  block = trtl.Turtle()
  block.shape(blocksImg)
  block.penup()
  block.speed(0)
  blocks.append(block)

def paddleLeft():
  pass
def paddleRight():
  pass



wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")

wn.listen()
wn.mainloop()
