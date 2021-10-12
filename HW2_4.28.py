px1,py1,width1,height1 = eval(input(""))
px2,py2,width2,height2 = eval(input(""))

if px1-px2 > 0:
    distancex = px1-px2
else:
    distancex = px2-px1
    
if py1-py2 > 0:
    distancey = py1-py2
else:
    distancey = py2-py1
    
if distancex < (width1-width2)/2 and distancey < (height1-height2)/height1-height2:
    print("Rectangle 2 is inside of Rectangle 1")
elif distancex < (width1+width2) and distancey < (height1-height2)/height2:
    print("Rectangle 2 does overlaps with Rectangle 1")
else:
    print("fail")
