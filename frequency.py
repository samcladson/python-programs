value = input("Enter any value : ")
dict1 = {}
dict3 = {}
dict4 = {}
c = 0
for i in value:
    counter = value.count(i)
    if i not in dict1:
        dict1[i]=counter
print(dict1)
dict2 = sorted(dict1.items(), key = lambda a: a[1], reverse = True)
dict3=dict(dict2)
print("sorted values : ", dict3)
print(dict3.values())
for i in dict3:
    if dict3.values() not in dict4:
        dict4[i]=dict3.values[i]
    elif dict3.values() in dict4:
        print("Two values have same frequency")
        break
else:
    print(max(dict3.values()))
print(dict4)
        
    
        

