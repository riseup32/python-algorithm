n, m = list(map(int, input().split()))  # 4 6
array = list(map(int, input().split()))  # 19 15 10 17

array.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return mid

for h in range(array[-1]-1, array[0], -1):
    idx = binary_search(array, h, 0, len(array) - 1)
    if sum([i-h for i in array[idx:] if i >= h]) >= m:
        print(h)
        break