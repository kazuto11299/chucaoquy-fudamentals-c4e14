
number = int(input("How many B bacterias? "))
time = int(input("Period of time (in minute)? "))
bacterias = int(number * 2 **(time / 2))
print("After {0} minutes, we will have {1} bacterias".format(time, bacterias))
