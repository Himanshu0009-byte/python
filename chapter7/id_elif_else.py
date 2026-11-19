#if elif else ladder

income=int(input("Enter you annual income: "))
if(income>=2000):
    print("You are eligible for home loan\n")
elif(income==0):
    print("please enter a valid income")
elif(income<0):
    print("you entered negative income please enter positive income")
else: 
    print("you are not eligible!!")