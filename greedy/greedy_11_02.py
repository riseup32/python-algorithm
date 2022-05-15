s = input()  # 02984

answer = int(s[0])
for i in s[1:]:
    if answer == 0 or int(i) == 0:
        answer += int(i)
    else:
        answer *= int(i)
        
print(answer)