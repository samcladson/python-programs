number = int(input("Enter a number :"))
value = str(number)
n = len(str(number))
sum = 0
for i in value:
    sum = sum + (int(i) ** n)
print(sum)
if sum==number:
    print ("armstrong number")
else:
    print("Not an armstrong number")
