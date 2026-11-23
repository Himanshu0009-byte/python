#Print the multiplication table of a given number in reverse order.
n=int(input("Enter a number:"))
for i in range(10,0,-1):
    print(n,"*",i,"=",n*i)