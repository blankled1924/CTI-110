# Donovan BLankley
# P4LAb1
# Write a turtle graphics programs that draws a triangle and a square using loops.

#import library
import turtle

win = turtle.Screen()
pen = turtle.Turtle()

win.bgcolor("lightblue")

pen.pensize(3)
pen.pencolor("green")
pen.shape("turtle")
pen.fillcolor("green")
pen.speed(3)

#code that draws shape

pen.begin_fill()

for side in range(4) :
    pen.forward(100)
    pen.left(90)

pen.left(90)
pen.forward(100)
pen.right(90)

sides = 3

while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

pen.end_fill()

win.mainloop()