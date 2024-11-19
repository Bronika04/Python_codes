x=int(input("Enter x coorinate"))
y=int(input("Enter y coorinate"))
if(x>0 and y>0):
    print("first")
elif(x<0 and y>0):
    print("second")
elif(x<0 and y<0):
    print("third")
else:
    print("fourth")
