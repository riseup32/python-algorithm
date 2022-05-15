def solution(food_times, k):
    i = 0
    for _ in range(k):
        if food_times[i] != 0:
            food_times[i] -= 1
            i += 1
            i %= len(food_times)
        else:
            while food_times[i] == 0:
                i += 1
                i %= len(food_times)
            food_times[i] -= 1
            i += 1
            i %= len(food_times)
    while food_times[i] == 0:
        i += 1
        i %= len(food_times)
    answer = i + 1
    return answer