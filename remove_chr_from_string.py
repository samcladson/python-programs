limit = int(input())
str2 = []
for i in range(limit):
    string = list(input())
    test_str = list(input())
    for j in range(len(string)):
            if string[j] not in test_str:
                str2.append(string[j])
    print(''.join(str2))
    str2 = []