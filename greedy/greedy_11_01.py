n = int(input())  # 5
array = list(map(int, input().split()))  # 2 3 1 2 2

array.sort()

answer = 0
i = 0
for _ in range(n):
    i += 1
    if len(array[:i]) >= array[:i][-1]:
        answer += 1
        for _ in range(i):
            array.pop(0)
        i = 0

print(answer)