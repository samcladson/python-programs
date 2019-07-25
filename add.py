ar = []
ar1=[]
count = 0
size = int(input("enter the size :"))
print ("Enter {} values".format(size))
for i in range(1,size+1):
    value = input("Enter {} value :".format(i))
    ar.append(value)
for i in ar:
    if ar[0]!=ar[1]:
        print (ar[0], end="")
    for i in range (1,size-1):
        if ar[i]!=ar[i+1] and ar[i]!=ar[i-1]:
            print(ar[i],end="")
        if ar[size-2]!=ar[size-1]:
            print(ar[size-2],end="")
