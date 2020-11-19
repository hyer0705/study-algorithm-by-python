# 2020-11-19(THU)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q13.치킨배달 P. 332
# link: https://www.acmicpc.net/problem/15686

# 내가 직접 작성한 코드
# max 값을 1e9로 바꾸고 성공!

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

# 도시의 치킨 거리 계산하는 함수
def calc_chicken_distance_sum(house_data, chicken_data):
    # 도시의 치킨 거리를 저장하는 변수
    chicken_distance_sum = 0
    # 집의 위치를 기준으로 치킨집 까지의 거리를 계산하여 가장 치킨 거리를 구하는 반복문
    for house in house_data:
        # 치킨 거리의 초기값은 1e9로 설정하여 최솟값을 구한다
        chicken_distance = 1e9
        # 치킨집의 위치 만큼 반복
        for chicken in chicken_data:
            # 현재 구한 거리를 저장하는 변수
            curr_distance = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            # 치킨 거리 계산
            chicken_distance = min(chicken_distance, curr_distance)
        # 도시의 치킨 거리에 방금 구한 치킨 거리를 더한다
        chicken_distance_sum += chicken_distance
    # 도시의 치킨 거리 반환
    return chicken_distance_sum

# result 는 도시의 치킨 거리 중 최솟값을 저장하는 변수로 1e9를 초기값으로 넣어준다
result = 1e9
# 파이썬의 조합 라이브러리를 사용하여 최대 m개의 치킨집의 조합을 구하고
# 도시의 치킨 거리 중 최솟값을 구한다
for chickens in itertools.combinations(chicken_data, m):
    result = min(result, calc_chicken_distance_sum(house_data=house_data, chicken_data=chickens))

# 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
# 도시의 치킨 거리(모든 집의 치킨 거리의 합)의 최솟값을 출력
print(result)