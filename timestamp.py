d1 = {}
n = int(input("Enter limit : "))
for i in range(n):
    key=input("Enter Time Stamp :")
    val1=input("No.Of persons : ")
    val2=input("Entry or Exit : ")

    d1.setdefault(key,[]).append(val1)
    d1.setdefault(key,[]).append(val2)
    print('')
print(d1)
lst1 = list(d1.items())
print(lst1)
for i in range(n):
    if (lst1[0][1][1]) && (lst1[1][1][1]) == 'enter':
        



