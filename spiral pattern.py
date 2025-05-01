import turtle
my_wn = turtle.Screen().bgcolor('White')
my_pen = turtle.Turtle()
num_sides = 4
size = 0
while True:
  for i in range(num_sides):
    my_pen.forward(size+1)
    my_pen.left(90)
    size = size-5
  size = size+1
  turtle.done()