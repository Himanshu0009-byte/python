number_1=int(input("Enter four number_1: "))
number_2=int(input("Enter four number_2: "))
number_3=int(input("Enter four number_3: "))
number_4=int(input("Enter four number_4: "))
if(number_1>number_2 and number_1>number_3 and number_1>number_4):
    print("Number 1 is greater number")
elif(number_2>number_3 and number_2>number_4 and number_2>number_1):
    print("Number 2 is greater")
elif(number_3>number_1 and number_3>number_2 and number_3>number_4):
    print("Numnber 3 is greater")
else:
    print("Number 4 is greater")