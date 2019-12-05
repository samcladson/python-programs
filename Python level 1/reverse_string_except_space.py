x = input()
l,l2 = [],[]
x1 = list(x)
rev = x[::-1]
rev2 = rev.split(' ')
rev2 = "".join(rev2)
rev3 = list(rev2)
num = 0
for i in range(len(x1)):
    if x1[i].isspace():
        l2.append(x[i])
    else:
        l2.append(rev3[num])
        num+=1
print("".join(l2))
