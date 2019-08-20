arr = [64,21,2,15,10,1,17]
swapped = False
for i in range(0,len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
    if swapped == False:
        break
print(arr)           
            