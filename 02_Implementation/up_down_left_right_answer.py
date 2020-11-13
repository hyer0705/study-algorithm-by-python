# 시뮬레이션 유형

# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 예제 4-1 상하좌우 정답 코드 p. 112

# N을 입력 받기
n = int(input())
x, y = 1, 1
move_plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

directions = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for move in move_plans:
    # 이동 후 좌표 구하기
    for i in range(len(directions)):
        if move == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)