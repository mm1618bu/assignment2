import math

q = int(input("Day of the month")) 
m = int(input("Month"))
j = float(input("Century"))
k = int(input("Year of the century"))
h = int(q+math.floor(26*(m+1)/10)+k+math.floor(k/4)+math.floor(j/4)+5*(j))%7
print(h)
