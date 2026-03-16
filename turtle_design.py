import turtle

t = turtle.Turtle()

turtle.bgcolor("black")

colors = ["red", "yellow", "blue", "pink", "green"]

for i in range(50):
    t.color(colors[i % 5])
    t.forward(i * 10)
    t.right(144)

turtle.done()