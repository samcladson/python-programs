import math
add=[]
fin =[]
# x = input().split(",")
# x = list(map(int,x))
x = [25,16,24,21,19]
for i in range(len(x)):
    s = math.sqrt(x[i])
    sqr = math.floor(s)
    sqrt = sqr*sqr
    if sqrt == x[i]:
        add.append(5)
    if x[i] % 4==0 and x[i] % 6==0:
        add.append(4)
    if x[i]%2==0:
        add.append(3)
    else:
        add.append(0)
    sumval = sum(add) 
    fin.append(sumval)
    add=[]
result = zip(fin,x)
result = list(result)
result.sort()
for i in range(len(result)):
    print(result[i][1],end = " ")


