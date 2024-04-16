from turtle import Turtle, Screen

jabya = Turtle()
jabya.shape("turtle")
my_screen = Screen()
for _ in range(4):

    jabya.forward(100)
    jabya.left(90)

my_screen.exitonclick()