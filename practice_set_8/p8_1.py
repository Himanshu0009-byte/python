#Write a python program to find a greatest of three number
def greatest():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    c=int(input("Enter the value of c:"))
    if (a == b ==c ):
        print("All three values are equal")
    elif(a>b and a>c):
        print("A is greatest number")
    elif(b>a and b>c):
        print("B is greater number:")
    elif(c>a and c>b):
        print(("C is greatest value:"))
    else:
        print("The two numbers are tied")


greatest()
    