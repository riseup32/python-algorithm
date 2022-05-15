from itertools import combinations

n, m = map(int, input().split())  # 8 5
array = list(map(int, input().split()))  # 1 5 4 3 2 4 5 2

li = list(combinations(array, 2))
answer = len([l for l in li if l[0] != l[1]])
print(answer)