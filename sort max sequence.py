value = input("Enter values seperated by commas : ")
val = value.split(',')
temp=[]
list1=[]
print(val)
n=len(val)
for i in range(n-1):
    for j in range(0,2):
        if val[i][j]<val[i+1][j]:
           temp=val[i]
           val[i]=val[i+1]
           val[i+1]=temp
maxval = ''.join(str(i) for i in val)
print(maxval)
