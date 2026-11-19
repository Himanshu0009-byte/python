#write a program to find out a given name is present in list or not
names_list=["himanshu","harry","Jassu","mittal"]
given_name=str(input("enter your name: "))
if(given_name in names_list):
    print("Given Name is Present in the list")
else:
    print("Unfortunately Given Name is Not Present")