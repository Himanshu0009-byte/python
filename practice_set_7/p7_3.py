#write a python program to print a table of number entered by user by using while loop

n=int(input("Enter the number to print the table: "))
i=1
while(i<11):
    print(n,"*",i,"=",n*i)
    i+=1