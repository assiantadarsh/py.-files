#problem 1 : find factorial of a number :
n = int (input("enter a number:"))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
print("FACTORIAL = ",fact)