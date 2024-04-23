"""EX08: Flower Power."""

__author__ = "730387535"

from turtle import Turtle, done, bgcolor, colormode, tracer, update

colormode(255)
# sky
bgcolor(179, 229, 252)

# grass
clover: Turtle = Turtle()
clover.penup()
clover.goto(-400, -100)
clover.pendown()
clover.color(102, 187, 106)
clover.begin_fill()
for i in range(2):
    clover.forward(800)
    clover.right(90)
    clover.forward(400)
    clover.right(90)
clover.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)  # Disable delay in tracing
    daisy: Turtle = Turtle()
    daisy.hideturtle()
    daisy.speed(0) 
    draw_sun(daisy, -300, 200, 50)
    draw_flower(daisy, 0, 0, 15, 10)
    draw_flower(daisy, -125, 4, 20, 8)
    draw_flower(daisy, 125, 4, 15, 8)
    draw_butterfly(daisy, 100, 100, 15)
    draw_butterfly(daisy, 0, 250, 15)
    draw_butterfly(daisy, 200, 185, 15)
    draw_butterfly(daisy, -100, 100, 15)
    draw_butterfly(daisy, -200, 200, 15)
    draw_daisy(daisy, -300, 50, 50)
    draw_daisy(daisy, -250, 50, 50)
    draw_daisy(daisy, 200, 50, 50)
    draw_daisy(daisy, 250, 50, 50)
    update()  # Now update the rendering
    done() 


def draw_sun(a_turtle: Turtle, x: float, y: float, sun_size: int) -> None:
    """Draw a sun for the garden! Line 55 changes the marker color!"""
    a_turtle.speed(10)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.pencolor("orange")
    a_turtle.fillcolor(255, 230, 90)
    a_turtle.begin_fill()
    a_turtle.circle(sun_size)
    a_turtle.end_fill()


def draw_flower(b_turtle: Turtle, x: float, y: float, petal_radius: float, petal_num: int) -> None:
    """Draw a recursive flower for the garden! Starting on line 67 through 77!"""
    draw_stem(b_turtle, x, y) 
    b_turtle.color(224, 134, 253) 
    
    if petal_num == 0:
        return 
    else:
        b_turtle.penup()
        b_turtle.goto(x, y)
        b_turtle.pendown()
        i: int = 0
        for i in range(6):
            b_turtle.circle(petal_radius)
            b_turtle.right(60)
        draw_flower(b_turtle, x, y, petal_radius * 0.8, petal_num - 1)


def draw_daisy(c_turtle: Turtle, x: float, y: float, daisy_radius: int) -> None: 
    """Draw a simple daisy for the garden!"""
    draw_stem(c_turtle, x, y) 
    c_turtle.color(255, 0, 22)
    c_turtle.penup()
    c_turtle.goto(x, y)
    c_turtle.pendown()
    
    for i in range(8):
        c_turtle.right(60)
        c_turtle.circle(daisy_radius, 90)
        c_turtle.left(90)
        c_turtle.circle(daisy_radius, 90)
        c_turtle.left(45)

    
def draw_butterfly(d_turtle: Turtle, x: float, y: float, wing_radius: int) -> None:
    """Draw a butterfly for the garden! Lines 103-108 fill the wings with a color other than white."""
    d_turtle.color(107, 115, 248)
    d_turtle.penup()
    d_turtle.goto(x, y)
    d_turtle.setheading(90)
    d_turtle.down()
    d_turtle.begin_fill()

    for i in range(4): 
        d_turtle.left(90)
        d_turtle.circle(wing_radius, 180)
    d_turtle.end_fill()
    draw_antenna(d_turtle, x - wing_radius, y - wing_radius, wing_radius + 15)


def draw_antenna(e_turtle: Turtle, x: float, y: float, antenna_length: float) -> None: 
    """Draw the antenna for the butterfly function drawn."""
    e_turtle.color(255, 255, 255)

    # left antenna 
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.setheading(90)
    e_turtle.pendown()
    e_turtle.circle(antenna_length, 50)
    e_turtle.dot(5, (107, 115, 248))

    # right antenna
    e_turtle.penup()
    e_turtle.goto(x, y)
    e_turtle.setheading(80)
    e_turtle.pendown()
    e_turtle.circle(-antenna_length, 50)
    e_turtle.dot(5, (107, 115, 248))


def draw_stem(f_turtle: Turtle, x: float, y: float) -> None:
    """Draw the flower stem with a leaf for the flower petals drawn!"""
    f_turtle.penup()
    f_turtle.pensize(2)
    f_turtle.goto(x, y)
    f_turtle.pendown()
    f_turtle.color(39, 111, 37)
    f_turtle.setheading(270)
    f_turtle.forward(50)
    
    # leaf
    f_turtle.begin_fill()
    f_turtle.circle(25, 90)
    f_turtle.left(90)
    f_turtle.circle(25, 90)
    f_turtle.end_fill()
    f_turtle.setheading(270)
    f_turtle.goto(x, -100) 


if __name__ == "__main__":
    main()