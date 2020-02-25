import math as m
val = list(map(int,input().split()))
r=val[0]
c=val[1]
mid= m.ceil(r/2)
a=0
for i in range(1,r+1):
    if i==mid:
        print('-'*((c-7)//2) +'WELCOME' +'-'*((c-7)//2))
    elif i<mid:
        if i==1:
            print('-'*((c//2)-i)+'.|.'*i+'-'*((c//2)-i))
        else:
            print('-'*((c//2)-(i*2)-(i-2))+'.|.'*((i*2)-1)+'-'*((c//2)-(i*2)-(i-2)))
            a=i
    elif i>mid:
         print('-'*((c//2)-(a*2)-(a-2))+'.|.'*((a*2)-1)+'-'*((c//2)-(a*2)-(a-2)))
         a-=1
