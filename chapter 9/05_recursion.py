#print multiplication of entered number
def fcatorial(n):
    if(n==1 or n==0):
        return 1
        return n * fcatorial(n-1)


n=int(input("Enter the value of n:"))

print(f"The factorial is: {fcatorial(n)}")
