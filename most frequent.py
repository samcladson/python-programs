value = input("Enter any string : ")
dict1={}
dict3={}
counter = 0
c = 0
for i in value:
    counter = value.count(i)
    if i not in dict1:
        dict1[i]=counter
dict2 = sorted(dict1.items(),reverse = True)
print(dict2)
dict3=dict(dict2)
print(dict3)
s = dict2[1][1]
for (key,val)in dict3.items():
    if val == s:
        c+=1
        k = [key]
if c > 1:
    print("More values have same frequency")
else:
    print(k)
    
