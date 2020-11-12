# 2020-11-12 (Thu)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q06. 무지의 먹방 라이브 정답 P.513

# 정답을 안보고 작성해보기

import heapq

def solution(food_times, k):
    answer = 0

    # 모든 음식을 먹는 시간이 k보다 작거나 같을 때 return -1
    if sum(food_times) <= k:
        return -1

    # 최소 힙 정렬 구현
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_eating_times = 0
    previous_eating_times = 0
    remain_food = len(food_times)

    # 현재 음식 시간에서 이전 음식 시간을 빼는 이유는 이전 음식 시간 만큼 다른 음식들도 먹은 상태여야하기 때문!
    while k - sum_eating_times >= ((q[0][0] - previous_eating_times) * remain_food):
        now_eating_time = heapq.heappop(q)[0]
        sum_eating_times += (now_eating_time - previous_eating_times) * remain_food
        remain_food -= 1
        previous_eating_times = now_eating_time

    result = sorted(q, key = lambda x: x[1])
    k -= sum_eating_times
    return result[k % remain_food][1]

food_times = [3, 1, 2]
k = 5


print(solution(food_times=food_times, k=k))