x = int(input())
num = 65
#main loop
for i in range(1,x+1):
    #loop for printing the spaces
    for j in range(i,(x+1)-1):
        print(" ",end=" ")
    #loop for printing the *
    for j in range(1,i+1):
        print("*",end = " ")
    print(end =" ")
    #loop for printing the alphabet
    for j in range(1,i+1):
        print(chr(num),end= " ")
        num += 1
    print("")
n,a,b,v = x,0,0,x
#second main loop
for i in range(1,x+1):
    #printing the spaces
    for j in range(1,i):
        print(" ",end= " ")
    #loop for printing number in decreasing order
    for j in range((n+1)-1,a,-1):
        print(j,end = " ")
    a+= 1
    print(end =" ")
    #loop for printing odd number
    for j in range(b,(v*2)):
        if j % 2 !=0:
            print(j,end=" ")
    b+=2
    print("")
