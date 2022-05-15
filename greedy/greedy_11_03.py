s = input()

list_0 = []
list_1 = []
while len(s) != 0:
    if s[0] == '0':
        p = s.find('1')
        if p != -1:
            list_0.append(s[:p])
        else:
            list_0.append(s[:])
            break
    else:
        p = s.find('0')
        if p != -1:
            list_1.append(s[:p])
        else:
            list_1.append(s[:])
            break
    s = s[p:]
    
answer = min(len(list_0), len(list_1))
print(answer)