# from turtle import *
# width(10)
# n = 1000
# for i in range(n):
#     for i in range(3):
#         color("red")
#         forward(20)
#         penup()
#
#
#         forward(20)
#         pendown()
#     for i in range(3):
#         color("blue")
#         forward(20)
#         penup()
#
#
#         forward(20)
#         pendown()
#
#
# mainloop()
from turtle import *

width(6)
color("pink")
n = int(input("Enter a number:"))
#
# for i in range(n):
#     forward(50)
#     penup()
#     forward(50)
#     pendown()

# mainloop()
for i in range(n):
    if i % 6 < 3:
        color("blue")
    else:
        color("red")
    forward(50)
    penup()
    forward(50)
    pendown()

mainloop()
