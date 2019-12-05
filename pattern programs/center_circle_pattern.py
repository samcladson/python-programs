n,x,a = 8,4,0
for i in range(n//2):
    for j in range(0,x):
        print("0",end = " ")
    for j in range(0,a):
        print("1",end=" ")
    for j in range(0,x):
        print("0",end=" ")
    a+=2
    x-=1
    print("")
n,x,a = 8,6,1
for i in range(n//2):
    for j in range(0,a):
        print("0",end = " ")
    for j in range(0,x):
        print("1",end=" ")
    for j in range(0,a):
        print("0",end = " ")
    a+=1
    x-=2
    print("")
    
