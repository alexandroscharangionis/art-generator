# import colorgram
# colors = colorgram.extract("painting.jpeg", 30)
import turtle as t
import random as r

t.colormode(255)
turtle = t.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.pendown()

hirst_colors = [(212, 154, 97), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54,
                                                                                                                                                                                                               120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81)]


def generate_painting(grid_size):
    turtle_pos = [turtle.pos()[0], turtle.pos()[1]]
    for row in range(grid_size):
        turtle.setpos(tuple(turtle_pos))
        for column in range(grid_size):
            dot_color = r.choice(hirst_colors)
            turtle.dot(20, dot_color)
            turtle.penup()
            turtle.forward(50)
        turtle_pos[1] += 50


generate_painting(10)


screen = t.Screen()
screen.exitonclick()
