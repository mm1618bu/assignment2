import math
from math import radians

radius = 6371


x1 = math.radians(35.2270869)
y1 = math.radians(-80.8431267)
x2 = math.radians(32.0835407)
y2 = math.radians(-81.0998342)
x3 = math.radians(28.5383355)
y3 = math.radians(-81.3792365)
x4 = math.radians(33.7489954)
y4 = math.radians(-84.3879824)


e = radius * math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))
print("Side 1: ", e)
g = radius * math.acos(math.sin(x2)*math.sin(x3)+math.cos(x2)*math.cos(x3)*math.cos(y2-y3))
print("Side 2: ",g)
h = radius * math.acos(math.sin(x4)*math.sin(x1)+math.cos(x4)*math.cos(x1)*math.cos(y4-y1))
print("Side 4: ",h)
f = radius * math.acos(math.sin(x3)*math.sin(x4)+math.cos(x3)*math.cos(x4)*math.cos(y3-y4))
print("Side 3: ",f )


a = 0.5*(e*g)
b = 0.5*(f*h)
c = a+b
print(c)
