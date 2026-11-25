#Write a program to convert celcius into farenhiet
def conversion():
    a=int(input("Enter the temprature in C"))
    if a<0 or a==0:
        return 0
    return ((a*(9/5))+32)


print(conversion())

