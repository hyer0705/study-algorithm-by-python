# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 예제 4-1. 상하좌우 -정답 코드 P.112

n = int(input())
x, y = 1, 1
move_data = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in move_data:
    for index in range(len(move_type)):
        if move == move_type[index]:
            nx = x + dx[index]
            ny = y + dy[index]
    # 맵을 벗어난 경우 continue
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x = nx
    y = ny

print(x, y)