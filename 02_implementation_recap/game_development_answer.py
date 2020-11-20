# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 실전문제. 게임 개발 - 정답 코드 P. 120

n, m = map(int, input().split())
visits = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
visits[x][y] = 1

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction = (direction - 1) % 4
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if maps[nx][ny] == 0 and visits[nx][ny] == 0:
        visits[nx][ny] = 1
        x = nx
        y = ny
        result += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(result)