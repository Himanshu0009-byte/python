1 #se N tak even numbers ka sum calculate karo
n=int(input("Enter a number:"))
sum=0
for j in range(0,n+1,2):
    sum+=j

print("The sum of even number is:",sum)
    