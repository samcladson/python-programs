value = input("Enter 2 digit number : ")
list1 = list(value)
a = int(list1[0])
b = int(list1[1])
add = a+b
mul = a*b
sum = add + mul
if sum == int(value):
    print("special number")
else:
    print("not a special number")