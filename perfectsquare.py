num = int(input("Enter a number : "))
for i in range(1,num+1):
    check = i**2
    if int(check) == num:
        print("Perfect Square")
        break
else:
    print("Not a perfect square")
        