#write a python program to write a reverse printed table
n=int(input("Enter number to print reverse table:"))
for i in range(10,0,-1):
    print(n,"*",i,"=",n*i)