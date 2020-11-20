# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 예제 4-1. 상하좌우 P.111

# n 입력
n = int(input())
# 지도 생성
maps = [[0] * (n + 1) for _ in range(n + 1)]
# 사용자의 처음 위치
x, y = 1, 1

# 여행가 이동할 계획서
move_data = list(input().split())

# x -> row, y -> col
# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

direction = 0

for move in move_data:
    if move == 'L':
        direction = 0
    elif move == 'R':
        direction = 1
    elif move == 'U':
        direction = 2
    elif move == 'D':
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx > 0 and nx <= n and ny > 0 and ny <= n:
        x = nx
        y = ny

print(x, y)