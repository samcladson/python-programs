n = 4
flag = 1
val=ord('A')
for i in range(n,0,-1):
    for j in range(1,i+1):
        if flag%2==0:
            print(j, end= " ")
        else:
            print(chr(val),end= ' ')
            val=val+1
    val=ord('A')
    print(" ")
    flag +=1
