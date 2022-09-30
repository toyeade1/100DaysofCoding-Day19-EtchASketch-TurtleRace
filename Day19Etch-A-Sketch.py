from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
