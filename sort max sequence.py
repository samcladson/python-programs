value = input("Enter values seperated by commas : ")
val = value.split(',')
temp=[]
list1=[]
print(val)
n=len(val)
for i in range(n-1):
    if val[i][0]<val[i+1][0]:
       temp=val[i]
       val[i]=val[i+1]
       val[i+1]=temp
maxval = ''.join(str(i) for i in val)
print(maxval)
