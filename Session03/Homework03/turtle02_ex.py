from turtle import *
colour = ['red', 'blue', 'brown', 'yellow', 'grey']
for a in range(5):
    begin_fill()
    color(colour[a])
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    penup()
    forward(50)
    pendown()
    end_fill()
mainloop()
