#Find the largest of three numbers.
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
c=int(input("Enter the value of c"))
if(a>b and a>c):
    if(a==b or a==c):
     print("a is qual to other number")
    
    print("A is greater number")
elif(b>a and b>c):
    if(b==a or b==c):
       print("b is euqal to other number")
    print("B is greater number")
else:
    print("C is greater number")