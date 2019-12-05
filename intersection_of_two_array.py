a = int(input())
b = int(input())
l1 = input().split(" ")
l2 = input().split(" ")
if len(l1)==a and len(l2)==b:
    val = zip(l1,l2)
    val = list(val)
    for i in range(len(val)):
        if val[i][0] == val[i][1]:
            print(val[i][0],end=" ")