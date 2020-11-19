# 2020-11-19(THU)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q13. 치킨 배달 - 정답 코드 P.527
# 완전 탐색 유형

# 조합 라이브러리 가져오기
from itertools import combinations

# n, m 입력
n, m = map(int, input().split())
house = []
chicken = []

# 집의 좌표, 치킨 집 좌표 입력
for row in range(n):
    data = list(map(int, input().split()))
    for col in range(n):
        if data[col] == 1:
            house.append((row, col)) # 일반 집
        if data[col] == 2:
            chicken.append((row, col)) # 치킨집

# 모든 치킨 집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = combinations(chicken, m)

# 치킨 거리의 합을 계산하는 함수
def calc_chicken_distance_sum(candidate):
    # 치킨 거리의 합
    chicken_distance_sum = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        chicken_distance = 1e9 # 10억
        # 치킨 집에 대하여
        for cx, cy in candidate:
            chicken_distance = min(chicken_distance, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        chicken_distance_sum += chicken_distance
    # 치킨 거리의 합 반환
    return chicken_distance_sum

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9 # 10억
for candidate in candidates:
    result = min(result, calc_chicken_distance_sum(candidate=candidate))

print(result)