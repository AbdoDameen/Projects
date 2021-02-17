import math

radius = int(input("please enter the radius of the circle:  "))

pi = math.pi
circ = 2 * pi * (radius)
area = pi * radius ** 2

print("The Circumference of the circle = " + format(circ, '.2f') + " And the Area of the circle = " + format(area, '.2f'))
