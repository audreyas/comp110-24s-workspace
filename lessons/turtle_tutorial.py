from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
leo.speed(50)
leo.hideturtle()
colormode(255)
leo.pencolor(222, 153, 252)
leo.fillcolor(222, 153, 252)
leo.begin_fill()
leo.penup()
leo.goto(-120, 0)
leo.pendown()
i: int = 0 
while (i < 3): 
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()
bob.pencolor(145, 52, 185)
bob.speed(100)
bob.hideturtle()
colormode(255)
bob.penup()
bob.goto(-120,0)
bob.pendown()
i: int = 0 
while (i < 3): 
    bob.forward(300)
    bob.left(120)
    i = i + 1

side_length: int = 300

i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1
    side_length = side_length * 0.97



done()










