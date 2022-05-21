n = int(input())  # 5
array = list(map(int, input().split()))  # -15 -6 1 3 7

def solution(array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1    
    return -1

solution(array)