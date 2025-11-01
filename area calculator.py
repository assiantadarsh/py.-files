print("****AREA CALCULATOR***")
print("""press 1 to get the area of square
press 2 to get the area of reactangle       
press 3 to get the area of circle    
press 4 to get the area of triangle     
      
     """ )

choice = int(input(" select the value 1-4:"))

if choice ==1:
    side = float(input("enter the side of square :"))
    area = side**2
    print( "the area is :" , area )
elif choice ==2:
    length = float(input("enter the length :"))
    width = float(input("enter the width :"))
    area = length*width
    print("reactangle area  :",area )
elif( choice ==3):
    r = int(input("enter the radius of cirlcle :"))
    area = 3.14*r*r
    print("circle area = ",area)
else:
    base = float(input(" enetr the base of reactangle:"))
    height = float(input(" enetr the height of reactangle:"))
    area = 0.5 *base*height
    print("triangle area = ",area)