#print the pattern
n=int(input("Enter number:"))
for i in range(n,0,-1):
    print("*"*(i),end="")
    print(" "*(i-1),end="")
    print(" ")