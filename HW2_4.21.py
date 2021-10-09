#! /usr/bin/python3
import math
 
n = 10#The Month in numerical form
k = 2021 #year of the century
j = 2021
q = 10# day of the month

"h = int(q+math.floor((26(n+1)/10))+k+math.floor(k/4)+math.floor(j/4)+5j)%7"
base = (26*(n+1))/10
base2 = k/4
base3 = j/4
base4 = 5*j
form2 = (q + base+k+base2+base3+base4)%7
print(int(form2))
