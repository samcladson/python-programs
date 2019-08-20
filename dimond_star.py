val=int(input("Enter limit : "))
for i in range(val,0,-1):
    for j in range(0,i+1):
        if j==i: 
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("\n")
for i in range(0,val):
    for j in range(0,i+1):
        if j==i: 
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print("\n")