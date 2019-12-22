import turtle
import math
turtle.setup(500, 500)
wn = turtle.Screen()
wn.bgcolor("black")
# wn.screensize(400, 400, "black")
tess = turtle.Turtle()
tess.color("white")
# tess.fillcolor("white")
tess.shape("blank")
tess.speed(0)

play = True
chart = [[0 for x in range(3)] for y in range(3)]
win = False

def printchart():
    global chart
    for i in chart:
        for j in i:
            print(j, end="\t")
        print()
    print()

def horizontal(c, i):
    tess.penup()
    tess.pensize(10)
    tess.setx(-225)
    tess.sety(400/3*(2 - i))
    tess.pendown()
    if c > 0:
        tess.color = "red"
        bruh = "RED WINS!"
    else:
        tess.color = "blue"
        bruh = "BLUE WINS!"
    tess.forward(450)
    tess.pensize(1)
    tess.penup()
    tess.setx(-65)
    tess.sety(-235)
    tess.pendown()
    tess.write(bruh, font = ("Georgia", 16, "bold"))


def vert(c, i):
    tess.penup()
    tess.pensize(10)
    tess.setx(400/3*(i - 2))
    tess.sety(-205)
    # tess.showturtle()
    tess.pendown()
    if c > 0:
        tess.color = "red"
        bruh = "RED WINS!"
    else:
        tess.color = "blue"
        bruh = "BLUE WINS!"
    tess.left(90)
    tess.forward(410)
    tess.left(-90)
    tess.pensize(1)
    tess.penup()
    tess.setx(-65)
    tess.sety(-235)
    tess.pendown()
    tess.write(bruh, font = ("Georgia", 16, "bold"))

def crow(c):
    tess.penup()
    tess.pensize(10)
    tess.setx(-210)
    tess.sety(-210)
    # tess.showturtle()
    tess.pendown()
    if c > 0:
        tess.color = "red"
        bruh = "RED WINS!"
    else:
        tess.color = "blue"
        bruh = "BLUE WINS!"
    tess.left(45)
    tess.forward(594)
    tess.left(-45)
    tess.pensize(1)
    tess.penup()
    tess.setx(-65)
    tess.sety(-235)
    tess.pendown()
    tess.write(bruh, font = ("Georgia", 16, "bold"))

def croy(c):
    tess.penup()
    tess.pensize(10)
    tess.setx(-210)
    tess.sety(210)
    # tess.showturtle()
    tess.pendown()
    if c > 0:
        tess.color = "red"
        bruh = "RED WINS!"
    else:
        tess.color = "blue"
        bruh = "BLUE WINS!"
    tess.left(-45)
    tess.forward(594)
    tess.left(45)
    tess.pensize(1)
    tess.penup()
    tess.setx(-65)
    tess.sety(-235)
    tess.pendown()
    tess.write(bruh, font = ("Georgia", 16, "bold"))

def winner():
    global chart
    global win
    h1 = chart[0][0] + chart[0][1] + chart[0][2]
    h2 = chart[1][0] + chart[1][1] + chart[1][2]
    h3 = chart[2][0] + chart[2][1] + chart[2][2]
    
    v1 = chart[0][0] + chart[1][0] + chart[2][0]
    v2 = chart[0][1] + chart[1][1] + chart[2][1]
    v3 = chart[0][2] + chart[1][2] + chart[2][2]

    c1 = chart[0][0] + chart[1][1] + chart[2][2]
    c2 = chart[0][2] + chart[1][1] + chart[2][0]

    if(abs(h1) == 3):
        win = True
        horizontal(h1, 1)
    if(abs(h2) == 3):
        win = True
        horizontal(h2, 2)
    if(abs(h3) == 3):
        win = True
        horizontal(h3, 3)

    if(abs(v1) == 3):
        win = True
        vert(v1, 1)
    if(abs(v2) == 3):
        win = True
        vert(v2, 2)
    if(abs(v3) == 3):
        win = True
        vert(v3, 3)
    
    if(abs(c1) == 3):
        win = True
        croy(c1)
    if(abs(c2) == 3):
        win = True
        crow(c2)

    # print(win)
    # printchart()
    


def getPos(x,y):
    # print("(", x, ", ", y, ")")
    a = 0
    b = 0
    i = 0
    j = 0
    if x >= -200 and x < (-200/3):
        a = -200
        i = 0
    elif x>= -200/3 and x < 200/3:
        a = -200/3
        i = 1
    elif x >= 200/3 and x < 200:
        a = 200/3
        i = 2

    if y >= -200 and y < (-200/3):
        b = -200
        j = 2
    elif y>= -200/3 and y < 200/3:
        b = -200/3
        j = 1
    elif y >= 200/3 and y < 200:
        b = 200/3
        j = 0
    global play
    global chart
    if x > -200 and x < 200 and y > -200 and y < 200 and (chart[j][i] == 0) and not win:
        if play:
            chart[j][i] = 1
            cross(a + (200-90*math.sqrt(2))/3, b + (200-90*math.sqrt(2))/3)
            play = not play
        else:
            chart[j][i] = -1
            circle(a + 200/3, b + 50/3)
            play = not play
    # printchart()
    winner()
    

def title():
    tess.penup()
    tess.setx(-190)
    tess.sety(210)
    tess.pendown()
    tess.write("Tic-Tac-Toe \t By Ananda Badari", font = ("Georgia", 16, "normal"))

def drawbox(x, y, size):
    tess.penup()
    tess.setx(x)
    tess.sety(y)
    tess.pendown()
    for i in range(4):
        tess.forward(size)
        tess.left(90)

def axes(size):
    tess.penup()
    tess.setx(-200)
    tess.sety(-200)
    tess.forward(size/3)
    tess.left(90)
    tess.pendown()
    tess.forward(size)
    tess.left(-90)
    
    tess.penup()
    tess.setx(-200)
    tess.sety(-200)
    tess.forward(2*size/3)
    tess.left(90)
    tess.pendown()
    tess.forward(size)
    tess.left(-90)

    tess.penup()
    tess.setx(-200)
    tess.sety(-200)
    tess.left(90)
    tess.forward(size/3)
    tess.pendown()
    tess.left(-90)
    tess.forward(size)

    tess.penup()
    tess.setx(-200)
    tess.sety(-200)
    tess.left(90)
    tess.forward(2*size/3)
    tess.pendown()
    tess.left(-90)
    tess.forward(size)

def circle(x, y):
    tess.pensize(3)
    tess.color("blue")
    tess.penup()
    tess.setx(x)
    tess.sety(y)
    tess.pendown()
    tess.circle(50)
    tess.pensize(1)
    # tess.color("white")

def cross(x, y):
    tess.pensize(3)
    tess.color("red")
    tess.penup()
    tess.setx(x)
    tess.sety(y)
    tess.left(45)
    tess.pendown()
    tess.forward(120)
    tess.penup()
    tess.forward(-60)
    tess.left(90)
    tess.pendown()
    tess.forward(60)
    tess.penup()
    tess.forward(-60)
    tess.pendown()
    tess.forward(-60)

    tess.penup()
    tess.setx(x)
    tess.sety(y)
    tess.left(-135)
    tess.pendown()
    tess.pensize(1)
    # tess.color("white")

def setup():
    title()
    drawbox(-200, -200, 400)
    axes(400)

def draw():
    s = tess.getscreen()
    s.onclick(getPos)

def main():
    global win
    # True is player 1, Cross
    # False is player 2, Circle
    draw()
    
    

setup()
main()

wn.mainloop()