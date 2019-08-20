n = int(input("Enter value : "))
val = n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==val or j>val:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print(" ")
    val=val-1