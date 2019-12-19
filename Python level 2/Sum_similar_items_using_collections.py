import collections as c
x=int(input())
l=[]
d,d2={},{}
for i in range(x):
    v= input().split(" ")
    l.append(v)
    if l[0][0] in d or l[0][0]+" "+l[0][1] in d:
        if len(v)>2:
            d2.setdefault(l[0][0]+" "+l[0][1],int(l[0][2]))
        else:
            d2.setdefault(l[0][0],int(l[0][1]))
    else:
        if len(v)>2:
            d.setdefault(l[0][0]+" "+l[0][1],int(l[0][2]))
        else:
            d.setdefault(l[0][0],int(l[0][1]))
    l=[]
d=c.Counter(d)
d2=c.Counter(d2)
res=(d+d2)
res = c.OrderedDict(res)
for i,j in sorted(res.items()):
    print("{} {}".format(i,j))
