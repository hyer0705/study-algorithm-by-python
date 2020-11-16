# 2020-11-16 (Mon)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 실전 문제. 게임 개발 정답 코드 P. 120

# 게임 맵의 크기 입력
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
characters_visit_map = [[0] * m for _ in range(n)] # 리스트 컴프리헨션 문법(알아두기!)

# 현재 캐릭터의 X 좌표, Y좌표, 방향(direction) 입력받기
x, y, direction = map(int, input().split())
characters_visit_map[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 캐릭터가 움직일 때의 좌표 계산을 위한 정보를 담는 리스트
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 캐릭터가 방문한 칸을 카운트하는 변수
count = 1
# 캐릭터가 왼쪽 방향으로 회전한 횟수를 저장하는 변수
turn_time = 0  

# 시뮬레이션 시작
while True:
    # 왼쪽으로 회전
    turn_left()
    # 이동할 x 좌표
    next_x = x + dx[direction]
    # 이동할 y 좌표
    next_y = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if maps[next_x][next_y] == 0 and characters_visit_map[next_x][next_y] == 0:
        maps[next_x][next_y] = 1 # 맵 이동
        x = next_x
        y = next_y
        # 방문한 칸 카운트
        count += 1
        # 회전한 회수 0으로 초기화
        turn_time = 0
        continue # 아래 코드는 실행시키지 않고 반복문의 조건으로 바로 이동
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        # 이동 없이 회전한 횟수만 증가
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 바라보는 방향으로 뒤로가야 하므로 현재 좌표에서 dx, dy 를 빼준다
        next_x = x - dx[direction]
        next_y = y - dy[direction]
        # 뒤로 갈 수 있다면 이동한다
        if maps[next_x][next_y] == 0:
            x = next_x
            y = next_y
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)