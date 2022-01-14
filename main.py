#Imports
import turtle as trtl
import random as rand
import threading

# Init. turtle stuff
wn = trtl.Screen()
wn.bgcolor('black')
# Add images
blocksGreen = "img/green.gif"
blocksYellow = "img/yellow.gif"
blocksRed = "img/red.gif"
playerImg = "img/paddle.gif"
ballImg = "img/ball.gif"
wn.addshape(blocksGreen)
wn.addshape(blocksYellow)
wn.addshape(blocksRed)
wn.addshape(playerImg)
wn.addshape(ballImg)

# Init global variables before start
blocks = []
blocksWd = 50
blocksHt = 20
blocksGap = 4
blocksNumX = 17
blocksNumY = 5
blocksTotal = blocksNumX * blocksNumY + 1

ballSpeed = 12
playerDir="None"
started = False

# Functions
def gameSpawn(): # Spawn blocks and stuff
    global blocksWd, blocksHt, blocksGap, blocksNumX, blocksNumY
    totalWd = (blocksNumX*blocksWd)+((blocksNumX-1)*blocksGap)
    totalHt = (blocksNumY*blocksHt)+((blocksNumY-1)*blocksGap)
    incrementX=blocksWd+blocksGap
    incrementY=blocksHt+blocksGap
    currentX=(-totalWd)/2
    currentY=((-totalHt)/2)+200
    currentX+=blocksWd/2
    currentY+=blocksHt/2
    counterX=0
    counterY=0
    while counterY<blocksNumY:
      if counterY==0:
          currentShape = blocksRed
      elif counterY==2:
          currentShape = blocksYellow
      elif counterY==4:
          currentShape = blocksGreen
      while counterX<blocksNumX:
          block=trtl.Turtle()
          blocks.append(block)
          block.speed(0)
          block.penup()
          block.goto(currentX,currentY)
          block.shape(currentShape)
          currentX+=incrementX
          counterX+=1
      currentX=(-totalWd)/2
      currentX+=blocksWd/2
      currentY+=incrementY
      counterX=0
      counterY+=1

def gameWrite(msg, color):
  if started != False:
    text=trtl.Turtle()
    text.color(color)
    text.penup()
    text.hideturtle()
    text.write(msg, font=('Courier', 30, 'bold'), align='center')
    text.hideturtle()

lives=3
daed=trtl.Turtle()
daed.color("White")
daed.penup()
daed.hideturtle()
daed.goto(-400,-320)
daed.write('Lives: ' + str(lives), font=('Courier', 10, 'bold'), align='center')
def death():
  global lives, started
  if (lives != 0):
    daed.penup()
    daed.goto(-400,-320)
    global deaths,fonta
    daed.clear()
    ball.setheading(0)
    ball.left(rand.randint(30,150))
    ball.goto(ply.xcor(),-290)
    lives-=1
    daed.write('Lives: ' + str(lives), font=('Courier', 10, 'bold'), align='center')
  else:
    gameWrite('Game Over', 'red')
    started = False

def detectCollision():
  global blocksTotal
  for i in range(len(blocks)):
    if ball.xcor() < ply.xcor()-30 + 60 and\
        ball.xcor() + 10 > ply.xcor()-30 and\
        ball.ycor() < ply.ycor() + 10 and\
        ball.ycor() + 10 > ply.ycor():
      ballCollideH()
    elif ball.xcor() < blocks[i].xcor()-25 + 50 and\
        ball.xcor() + 10 > blocks[i].xcor()-25 and\
        ball.ycor() < blocks[i].ycor() + 20 and\
        ball.ycor() + 10 > blocks[i].ycor():
      if (blocks[i].shape() == "img/red.gif"):
        blocks[i].goto(1000,1000)
        blocksTotal -= 1
      elif (blocks[i].shape() == "img/yellow.gif"):
        blocks[i].shape("img/red.gif")
      elif (blocks[i].shape() == "img/green.gif"):
        blocks[i].shape("img/yellow.gif")
      ballCollideH()
  if ball.xcor()<-475:
    ballCollideV()
  elif ball.xcor()>475:
    ballCollideV()
  elif ball.ycor()>380:
    ballCollideH()
  elif ball.ycor()<-500:
      death()
def ballCollideH():
  degree = (180-ball.heading())*2
  ball.setheading(ball.heading()+degree)
  ball.forward(12)
def ballCollideV():
  degree = (90-ball.heading())*2
  ball.setheading(ball.heading()+degree)
  ball.forward(12)
def moveBall(): # Move ball, called constantly
  global started, playerDir
  started = True
  while (True and blocksTotal != 1):
    detectCollision()
    ball.forward(ballSpeed)
    if playerDir == 'None':
      ply.goto(ply.xcor(), ply.ycor())
    if playerDir == 'Left':
      ply.goto(ply.xcor()-30, ply.ycor())
    if playerDir == 'Right':
      ply.goto(ply.xcor()+30, ply.ycor())
    playerDir = 'None'
  gameWrite('Game Complete', 'green')
  
runBall = threading.Thread(target=moveBall)

def paddleLeft(): # Move player left and right
  global playerDir
  if (started == False):
    runBall.start()
  if (ply.xcor() != -450):
    playerDir = 'Left'
def paddleRight():
  global playerDir
  if (started == False):
    runBall.start()
  if (ply.xcor() != 450):
    playerDir = 'Right'


border = trtl.Turtle()
border.pencolor("white")
border.pensize(8)
border.penup()
border.speed(0)
border.setpos(-482, -500)
border.pendown()
border.left(90)
border.forward(910)
border.right(90)
border.forward(960)
border.right(90)
border.forward(1000)

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
ball.left(rand.randint(30,150))

gameSpawn()

wn.onkeypress(paddleLeft, "a")
wn.onkeypress(paddleRight, "d")
wn.onkeypress(paddleLeft, "Left")
wn.onkeypress(paddleRight, "Right")

wn.listen()
wn.mainloop()
