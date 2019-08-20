def pattern(n):
    val=n
    for i in range(1,n+1):
        for j in range(1,val+1):
            print(' ',end= " ")
        for k in range(1,i+1):
            print("+"," ", end=" ")
        print(" ")
        val=val-1
    val=n
    for i in range(1,n+1):
        for j in range(1,i+2):
            print(' ',end= " ")
        for k in range(1,val):
            print("+",' ',end=" ")
        print(" ")
        val=val-1
n = int(input("Enter limit : "))
pattern(n)