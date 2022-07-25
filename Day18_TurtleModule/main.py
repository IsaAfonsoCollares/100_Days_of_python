import turtle as t
#import colorgram
from random import choice
t.colormode(255)

# image_colours = colorgram.extract('image.jpg', 30)
# colours_rgb = []
# for color in image_colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     colours_rgb.append(color)
# print(colours_rgb)
colours_rgb = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53),
           (219, 205, 120), (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53),
           (184, 141, 158), (132, 182, 145), (48, 56, 99), (180, 97, 107), (56, 35, 22),
           (68, 130, 106), (98, 118, 166), (82, 148, 159), (221, 175, 187), (169, 206, 166),
           (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211), (80, 70, 39)]


def choose_color():
    colours = choice(colours_rgb)
    return colours


def draw_dot():
    pencil.pendown()
    color = choose_color()
    pencil.dot(25, color)
    pencil.penup()


pencil = t.Turtle()
pencil.penup()
pencil.setheading(135)
pencil.forward(300)
pencil.setheading(0)
pencil.hideturtle()


for j in range(0, 10):
    for i in range(0, 10):
        draw_dot()
        pencil.forward(50)
    pencil.backward(500)
    pencil.right(90)
    pencil.forward(50)
    pencil.left(90)

screen = t.Screen()
screen.screensize(800, 800)
screen.exitonclick()
