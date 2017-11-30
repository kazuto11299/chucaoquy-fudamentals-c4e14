from turtle import *
n = 7
speed(-1)
colour = ('red', 'blue', 'brown', 'yellow', 'grey')
for i in range(3, n + 1):
    color(colour[i - 3])
    for a in range(i):
        forward(100)
        left(360/i)
mainloop()
