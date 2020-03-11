from collections import defaultdict as d_dict
data = d_dict()
string = list(input())
count = 0
for i in string:
    if i not in data:
        count+=1
        data.setdefault(i,count)
    elif i in data:
        data[i]=count
print(min(data.items())[1])
