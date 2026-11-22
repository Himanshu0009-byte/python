#write a python program too caculate the factorial of given number
n = int(input("Enter a number:"))
result = 1

while n > 0:
    result *= n
    n -= 1

print(result)
