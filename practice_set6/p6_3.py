phrase_1="Click on this ad"
phrase_2="Make a lot of money"
phrase_3="Click"
message = input("Enter the cfeedback that you want: \n")
if(phrase_1 in message or (phrase_2 in message) or (phrase_3 in message)):
    print("Your entered message is similar to spam word so please reenter it")
else:
    print("your feedback is awsome!!")