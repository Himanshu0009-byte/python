#write a python program to print following star pattern
n=int(input("Enter a number:"))
i=1
for i in range(1,n+1):
    print("*"*(i),end="")
    print(""*(i-1),end="")
    print("")
    
    