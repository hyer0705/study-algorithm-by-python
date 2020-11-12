# Q. 무지의 먹방 라이브
# p. 316

import heapq

def solution(food_times, k):
    answer = 0

    # 모든 음식을 먹는 초가 k보다 작거나 같을 때 return -1
    if sum(food_times) <= k:
        return -1

    # 최소 힙 정렬 구현
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    # 지금까지 먹는데 사용한 시간을 더하는 변수
    sum_eating_times = 0
    # 이전 타임에 먹은 음식의 소요시간을 저장하는 변수
    previous_eating_time = 0
    # 아직 남아있는 음식의 갯수를 저장하는 변수
    remain_foods = len(food_times)

    # k 초 - 지금까지 먹는데 사용한 시간을 더한 변수가 (우선순위 큐에서 현재 가장 짧은 시간을 가진 음식의 시간 - 이전에 먹은 음식의 시간) * 남아있는 음식의 갯수보다
    # 크거나 같을 때만 반복
    while k - sum_eating_times >= (q[0][0] - previous_eating_time) * remain_foods:
        # 우선순위 큐에서 뽑은 현재 가장 짧은 시간으로 먹을 수 있는 음식의 시간
        now_eating_time = heapq.heappop(q)[0]
        # 지금까지 먹는데 사용한 시간을 더해줌
        sum_eating_times += (now_eating_time - previous_eating_time) * remain_foods
        # 먹은 음식 제거
        remain_foods -= 1
        # 이전에 먹은 음식의 시간 저장
        previous_eating_time = now_eating_time

    # 남은 음식들 중 음식 번호를 기준으로 정렬
    result = sorted(q, key=lambda x: x[1])
    # k초 에서 지금까지 먹는데 사용한 시간들을 빼줌
    k -= sum_eating_times
    # result[남은 k초를 남은 음식으로 나눈 나머지][음식번호를 뜻하는 두번째 열]
    return result[k % remain_foods][1]

food_times = [3, 1, 2]
k = 5

print(solution(food_times = food_times, k = k))