# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter04. 구현

# 실전문제. 왕실의 나이트
# 내가 작성한 코드

# 말의 좌표 입력
coordinates = input()
col = ord(coordinates[0]) - ord('a') + 1
row = int(coordinates[1])

# 나이트가 이동할 좌표 경우의 수
# (row, col)
steps = [
    (-1, 2)
    , (1, 2)
    , (-1, -2)
    , (1, -2)
    , (-2, 1)
    , (-2, -1)
    , (2, 1)
    , (2, -1)
]

cnt = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if nrow > 0 and nrow < 9 and ncol > 0 and ncol < 9:
        cnt += 1

print(cnt)