empname = input("Enter Employee's Name: ")
weekhrs = float(input("Enter number of hours worked in a week: "))
payrate = float(input("Enter hourly pay rate: "))
fedwith = float(input("Enter federal tax witholding rate: "))
stawith = float(input("Enter state tax witholding rate: "))

gross = float(weekhrs * payrate)
fed = gross * .2
state = gross * .09
deduct = fed + state
net = float(gross-deduct)

print("Employee Name: ", empname)
print("Hours Worked: ", weekhrs)
print("Pay Rate: $", payrate)
print("Gross Pay: $", gross)
print("Deductions: ")
print("     Federal Witholding (20%): $", fed)
print("     State Witholding (9%): $", state)
print("     Total Deudction: $", deduct)
print("Net Pay: $", net)
