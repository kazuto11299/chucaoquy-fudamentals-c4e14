x = int(input("x = "))
operation = str(input("Operation(+,-,*,/): "))
y = int(input("y = "))
print("* " * 20)
if operation == "*":
    multiplication = x * y
    print(int(x), "*", int(y), "=", multiplication)
elif operation == "+":
    sum = x + y
    print(int(x), "+", int(y), "=", sum)
elif operation == "-":
    minus = x - y
    print(int(x), "-", int(y), "=", minus)
elif operation == "/":
    divide = x / y
    print(int(x), "/", int(y), "=", divide)
