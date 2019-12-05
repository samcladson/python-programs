test_case = int(input())
for i in range(test_case):
    val = list(input())
    temp = ''.join(val)
    val = map(int,val)
    val = list(val)
    if len(val)> 2 or len(val)==1:
        print("Invalid input")
    else:
        s = val[0]+val[1]
        p = val[0]*val[1]
        res = s+p
        if res == int(temp):
            print("Special number")
        else:
            print("Not a special number")