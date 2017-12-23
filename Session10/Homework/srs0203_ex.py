from mlab import *
from Models.service import *

mlab_connect()

print("2. List ALL rivers in ’Africa’ continent")
a = river.objects(continent = 'Africa')
for i in a:
    print(i)

print("3. list ALL rivers in ‘S. America’ continent with length less than 1000 km")
n = river.objects(continent = 'S. America', length__lt = 1000)
for x in n:
    print(x)
