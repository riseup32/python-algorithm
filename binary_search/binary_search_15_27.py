import collections

n, x = map(int, input().split())  # 7 2
array = list(map(int, input().split()))  # 1 1 2 2 2 2 3

def solution(x, array):
    count_dict = collections.Counter(array)
    return count_dict[x] if x in count_dict.keys() else -1

solution(x, array)