#write a username and check whether the given username contains less than 10 words or not

user_name=input("Enter your user name: ")

if(len(user_name)<10):
    print("Your user name conatins less than 10 words : ",len(user_name))
else:
    print("Exceeds more than 10 words: ",len(user_name))