n, m = map(int, input().split())  # 2 4
array = [list(map(int, input().split())) for _ in range(n)]  # 7 3 1 8 # 3 3 3 4

print(max([min(li) for li in array]))