from bisect import bisect_right

n = int(input())  # 5
array = list(map(int, input().split()))  # 3 2 1 1 9

array.sort()
m = max(array)
for i in range(1, n * m):
    answer = i
    array_ = array.copy()
    while i != 0:
        p = bisect_right(array_, i)
        if p == 0:
            break
        else:
            i -= array_[p-1]
            array_.pop(p-1)
    if i != 0:
        break

print(answer)