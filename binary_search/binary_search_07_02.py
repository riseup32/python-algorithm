n = int(input())  # 5
array = list(map(int, input().split()))  # 8 3 7 9 2
m = int(input())  # 3
targets = list(map(int, input().split()))  # 5 7 9

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
    return None

for i in range(m):
    answer = binary_search(array, targets[i], 0, len(array) - 1)
    if answer == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')