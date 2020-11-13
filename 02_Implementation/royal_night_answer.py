# 2020-11-13(Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 실전 문제. 왕실의 나이트 정답 코드 P. 117

# 현재 나이트의 위치 입력받기
coordinates = input()
row = int(coordinates[1])
col = int(ord(coordinates[0])) - int(ord('a')) + 1

# 체스판의 벗어나면 안되는 위치들을 변수에 저장
MIN_LOCATION = 1
MAX_LOCATION = 8

# 나이트가 이동할 수 있는 8가지 방향 정의
# (row - 상하, col - 좌우)
steps = [
    (-2, -1)
    , (-2, 1)
    , (-1, -2)
    , (-1, 2)
    , (2, -1)
    , (2, 1)
    , (1, -2)
    , (1, 2)
]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= MIN_LOCATION and next_row <= MAX_LOCATION and next_col >= MIN_LOCATION and next_col <= MAX_LOCATION:
        result += 1

# 경우의 수 출력
print(result)