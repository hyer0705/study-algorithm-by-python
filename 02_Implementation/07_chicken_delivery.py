# 2020-11-19(THU)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q13.치킨배달 P. 332
# link: https://www.acmicpc.net/problem/15686

# 내가 직접 작성한 코드
# 책에 있는 테스트만 맞음...

import itertools

# n, m 입력
n, m = map(int, input().split())
# 도시의 정보 입력
city_data = []
for _ in range(n):
    city_data.append(list(map(int, input().split())))

# 1. 치킨 집 갯수 세기
chicken_cnt = 0
house_data = [] # 집이 있는 좌표를 넣을 리스트
chicken_data = [] # 치킨 집이 있는 좌표를 넣을 리스트
for row in range(len(city_data)):
    for col in range(len(city_data[row])):
        curr_coordinates = city_data[row][col]
        # 현재 좌표가 집인 경우 house_data에 append
        if curr_coordinates == 1:
            house_data.append((row, col))
        # 현재 좌표가 치킨 집인 경우 chicken_data에 append 그리고 chicken_cnt 카운트
        elif curr_coordinates == 2:
            chicken_cnt += 1
            chicken_data.append((row, col))

def calc_chicken_distance_sum(house_data, chicken_data):
    chicken_distance_sum = 0
    for house in house_data:
        chicken_distance = n
        for chicken in chicken_data:
            curr_distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            chicken_distance = min(chicken_distance, curr_distance)
        chicken_distance_sum += chicken_distance
    return chicken_distance_sum

# 치킨 집의 갯수와 m과 같다면 경우의 수는 1번이므로
result = 2500
if chicken_cnt == m:
    result = calc_chicken_distance_sum(house_data=house_data, chicken_data=chicken_data)
else:
    for chickens in itertools.combinations(chicken_data, m):
        result = min(result, calc_chicken_distance_sum(house_data=house_data, chicken_data=chickens))

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
# 도시의 치킨 거리(모든 집의 치킨 거리의 합)의 최솟값을 출력
print(result)