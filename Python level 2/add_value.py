import collections as c
x=int(input())
l=[]
d,d2={},{}
for i in range(x):
    v= input().split(" ")
    l.append(v)
    if l[0][0] in d:
        d2.setdefault(l[0][0],l[0][1])
    else:
        d.setdefault(l[0][0],l[0][1])
    l=[]
print(d)
print(d2)
