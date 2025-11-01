x = 12
y = 13
"""temp = y
y = x
x = temp
print(x)
print(y)"""
#without temp varriable method 1:
"""x,y=y,x
print(x)
print(y)"""
#without temp varriable method 2:
x = x+y
y = x-y
x = x-y
print(x)
print(y)


