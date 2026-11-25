def star():
    n=int(input("Enter the value of n:"))
    for i in range(n,0,-1):
        print("*"*(i),end="")
        print(""*(i-1),end="")
        print(" ")


print(star())