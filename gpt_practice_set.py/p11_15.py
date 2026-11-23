#Check whether a person is eligible to vote.
age=int(input("Enter your age:"))
if(age>=18):
    print("Congratulations!! You are eligible for vote")
elif(age<0):
        print("!!Please enter valid age!!")
else:
      print("You are not eligible for vote")
