marks_1=int(input("Enter a marks of subject 1: "))
marks_2=int(input("Enter a marks of subject 2: "))
marks_3=int(input("Enter a marks of subject 3: "))

if(marks_1%300>=33):
    print("you passed in subject 1")

if(marks_2%300>=33):
        print("you passed in subject 2")
if(marks_3%300>=33):
            print("you passed in subject 3")
if(marks_1+marks_2+marks_3%300>=40):
        print("you are passed")
else:
        print("You are failed in the examination")

            
