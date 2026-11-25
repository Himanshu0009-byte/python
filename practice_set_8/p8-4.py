#Write a recursive function to print sum of first n natural numbersdef
def calculate(n):
    if n==0 :
        return 0
    return n+calculate(n-1)


print(calculate(7))
