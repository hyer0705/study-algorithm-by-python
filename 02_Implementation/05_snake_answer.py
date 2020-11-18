# 2020-11-18(Wed)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q11. 뱀 정답 코드
# link: https://www.acmicpc.net/problem/3190

# 보드의 크기 입력
n = int(input())
# 사과의 개수 입력
k = int(input())
# 맵 정보
maps = [[0] * (n + 1) for _ in range(n + 1)]
# 방향 회전 정보
info = []

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    row, col = map(int, input().split())
    maps[row][col] = 1
    
# 뱀의 방향 변환 횟수 입력
l = int(input())
# 방향 회전 정보 입력
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c)) # (시간, 방향 회전 정보)

# =================================================
# 정보 입력
# =================================================

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전 함수 정의
def turn(direction, c):
    # 왼쪽 방향으로 회전할 떄
    if c == 'L':
        direction = (direction - 1) % 4
    # 오른쪽 방향으로 회전할 때
    else:
        direction = (direction + 1) % 4
    return direction

# 시뮬레이션 함수
def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    maps[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 회전 정보를 담는 리스트의 인덱스
    snake = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽!)

    while True:
        # 뱀이 이동할 위치
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 아에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and maps[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                snake.append((nx, ny))
                px, py = snake.pop(0)
                maps[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if maps[nx][ny] == 1:
                maps[nx][ny] = 2
                snake.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            # 시간 증가
            time += 1
            break
        # 다음 위치로 머리를 이동
        x, y = nx, ny
        # 시간 증가
        time += 1
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            direction = turn(direction=direction, c=info[index][1])
            index += 1

    # time return
    return time

print(simulate())