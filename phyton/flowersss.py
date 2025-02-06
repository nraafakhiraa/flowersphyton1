import turtle

li = turtle.Turtle()
li .screen.bgcolor("light gray")
li.pensize(4)
li.color("green")
li.left(90)
li.backward(80)
li.speed(600)
li.shape("turtle")

def love(i):
    if i<20:
        return
    else:
        li.forward(i)
        li.color("red")
        li.circle(13)
        li.color("red")
        li.circle(10)
        li.color("red")
        li.circle(8)
        li.color("red")
        li.circle(6)
        li.color("white")
        li.circle(2)
        li.color("green")
        li.left(30)

        love(3*i/4)

        li.right(60)

        love(3*i/4)

        li.left(30)
        li.backward(i)
love(90)
turtle.done