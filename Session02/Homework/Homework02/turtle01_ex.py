from turtle import *
width(2)
color("red")
left(30)
for n in range(2):
    for i in range(2):
        forward(100)
        right(60)
        forward(100)
        right(120)
        forward(100)
        right(60)
        forward(100)
        left(60)
    left(90)

mainloop()
