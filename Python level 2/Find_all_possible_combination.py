import operator as o
op = [o.add,o.sub,o.mul,o.floordiv]
v = ['+','-','*','/']
l = [2,2,3]
t = 3
for i in range(len(op)):
    for j in range(len(op)):
        a = op[i](l[0],l[1])
        b = op[j](a,l[2])
        if b == t:
            print("{} {} {} {} {} {} {}".format(l[0],v[i],l[1],v[j],l[2],'=',b))
            break
