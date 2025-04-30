import turtle
turtle.Screen().bgcolor('red')
turtle.Screen().setup(300,400)
hexagon = turtle.Turtle()
num_sides = 6
side_len = 50
angle = 360/num_sides
for i in range(num_sides):
    hexagon.forward(side_len)
    hexagon.right(angle)
turtle.done()