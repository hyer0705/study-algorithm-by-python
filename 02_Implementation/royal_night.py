# 2020-11-13(Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 실전 문제. 왕실의 나이트 P.115

# 내가 작성한 코드

# 행: 1~8, 열: a~h
# coordinates 입력
coordinates = input()

# 체스판 크기
CHESS_BOARD = 8

col = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # 좌우
# 좌표를 모두 숫자로 변경
for i in range(1, len(col)):
    if coordinates[0] == col[i]:
        coordinates = str(i) + coordinates[1]

# (좌 우, 상 하)
directions = [
    (-2, -1) # 좌-좌-상
    , (-2, 1) # 좌-좌-하
    , (2, -1) # 우-우-상
    , (2, 1) # 우-우-하
    , (-1,-2) # 좌-상-상
    , (1, -2) # 우-상-상
    , (-1, 2) # 좌-하-하
    , (1, 2) # 우-하-하
]
# 나이트가 이동할 수 있는 경우의 수를 출력하시오.
cnt = 8

for direction in directions:
    n_row = int(coordinates[1]) + direction[1]
    n_col = int(coordinates[0]) + direction[0]
    if n_row < 1 or n_row > CHESS_BOARD or n_col < 1 or n_col > CHESS_BOARD:
        cnt -= 1

print(cnt)