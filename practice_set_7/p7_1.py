#Write a python program to print multiplication table of input provided by user
n=int(input("Enter the number so we can print the table of it: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)