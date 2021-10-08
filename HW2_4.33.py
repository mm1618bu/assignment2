d = int(input("Enter a decimal value (0 to 15): "))
if d > 15:
    print("error")
else:
    e = hex(d).split('x')[-1]
    print(e)
