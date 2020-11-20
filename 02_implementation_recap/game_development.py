# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 실전 문제. 게임 개발 P.118
# 내가 작성한

# n(세로), m(가로) 입력
n, m = map(int, input().split())
# 캐릭터의 위치와 바라보는 방향 입력
x, y, d = map(int, input().split())
# 지도 입력
maps = []
# 캐릭터가 방문한 곳을 저장하는 리스트
visit_maps = [[0] * m for _ in range(n)]

for _ in range(n):
    maps.append(list(map(int, input().split())))
maps[x][y] = 1 # 방문한 곳은 1로 표시

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left(direction):
    return (direction - 1) % 4

# 캐릭터가 방문한 칸의 갯수를 저장하는 변수
result = 1
# 왼쪽으로 회전한 횟수를 저장하는 변수
turn = 0
while True:
    d = turn_left(direction=d) # 왼쪽방향으로 turn
    turn += 1
    # 캐릭터가 다음으로 이동할 위치
    nx = x + dx[d]
    ny = y + dy[d]
    # 갈 수 있는 칸일 때
    if maps[nx][ny] == 0 and visit_maps[nx][ny] == 0:
        visit_maps[nx][ny] = 1
        x = nx
        y = ny
        turn = 0
        result += 1

    # 네 방향 모두 갔던 칸이거나 바다일 때
    if turn == 4:
        nx = x - dx[d]
        ny = x - dy[d]
        if maps[nx][ny] == 1:
            break
        x = nx
        y = ny
        turn = 0

print(result)