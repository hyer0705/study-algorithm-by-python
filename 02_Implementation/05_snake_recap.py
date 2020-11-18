# 2020-11-18(Wed)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q11. 뱀
# 정답을 보고 공부한 후 책 덮고 다시 코드 짜보기

# 보드의 크기 n 입력
n = int(input())
# 사과의 개수 k 입력
k = int(input())
# 지도 초기화
maps = [[0] * (n + 1) for _ in range(n + 1)] # 리스트 컴프리헨션 문법(꼭 기억하기!)
# 뱀의 방향 회전 정보를 저장하는 info 리스트
info = []

# k개의 사과 위치 입력
for _ in range(k):
    row, col = map(int, input().split())
    maps[row][col] = 1 # 사과의 위치는 1로 입력

# 뱀의 방향 변횐 횟수 l 입력
l = int(input())
# l개의 뱀의 방향 변환 정보 입력
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c)) # (x초, 문자 c)

# 방향 정보(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 회전 함수 정의
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 시뮬레이션 함수 정의
def simulation():
    x, y = 1, 1 # 뱀의 초기 위치
    maps[x][y] = 2 # 뱀이 위치한 곳은 2로 표시

    time = 0 # 시간 카운트를 저장하는 변수

    index = 0 # info 리스트의 인덱스를 저장하는 변수

    snake_coordinates = [(x, y)] # 뱀의 현재 위치(좌표)를 나타내는 리스트

    direction = 0 # 뱀은 처음에 동쪽으로 이동하므로 동쪽: 0을 저장함!
    # 시간 흐름!
    while True:
        # 뱀의 다음 위치
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 뱀이 맵을 벗어나지 않고, 자신의 몸에 닿지 않은 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and maps[nx][ny] != 2:
            # 사과가 있는 경우
            if maps[nx][ny] == 1:
                maps[nx][ny] = 2
                snake_coordinates.append((nx, ny))
            # 사과가 없는 경우
            if maps[nx][ny] == 0:
                maps[nx][ny] = 2
                snake_coordinates.append((nx, ny))
                px, py = snake_coordinates.pop(0)
                maps[px][py] = 0
        else:
            time += 1
            break
        x, y = nx, ny # 뱀 이동
        time += 1 # 시간 증가
        # 현재 시간이 info 에 있는 time 과 같을 때 회전을 할 때가 됐다는 뜻!
        if index < l and info[index][0] == time:
            direction = turn(direction=direction, c=info[index][1])
            index += 1

    return time

print(simulation())