x1,y1=map(float,input("Enter x1 and y1: ").split())
x2,y2=map(float,input("Enter x2 and y2: ").split())
length=((x2-x1)**2+(y2-y1)**2)**(1/2)
print("The distance of the two points is "+str(length))