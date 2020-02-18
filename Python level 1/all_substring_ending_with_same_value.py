def findAllSameSubstring(s):
    d = ''; 
    n = len(s);  
    for i in range(n): 
        for j in range(i, n):
                if (s[i] == s[j]): 
                    for k in s[i:j+1]:
                       d=d+k
                    if d[0]=='1' and d[-1]=='1' and len(d)>1:
                        print(d)
                    d=''

s="1010010001"
findAllSameSubstring(s)
