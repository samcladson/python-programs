number = int(input("Enter a number :"))
n = len(str(number))
a = number % 10
sum = sum + (a ** n)
number=number // 10
print (a)