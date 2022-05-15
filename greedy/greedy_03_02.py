n, m, k = map(int, input().split()) # 5 8 3
array = list(map(int, input().split()))  # 2 4 5 4 6

array.sort(reverse=True)

answer = 0
i = 0
for _ in range(m):
    if i != k:
        answer += array[0]
        i += 1
    else:
        answer += array[1]
        i = 0
        
print(answer)
