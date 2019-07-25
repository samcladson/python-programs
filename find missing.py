num = int(input("Enter limit : "))
list1=[]
list2=[]
for i in range(1,num+1):
    value = int(input("Enter value : "))
    list1.append(value)
mx = max(list1)
mn = min(list1)
for i in range(mn,mx+1):
    if i not in list1:
        list2.append(i)
print("The missing numbers are : ",list2)
    
