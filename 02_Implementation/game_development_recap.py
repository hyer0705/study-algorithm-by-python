# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 실전 문제. 게임 개발 P.118

# 복습

# 지도의 크기 입력
n, m = map(int, input().split())

# 캐릭터가 방문한 곳을 저장하는 맵 선언
visits = [[0] * m for _ in range(n)] # 리스트 컴프리헨션 문법(꼭 기억해두기)

# 캐릭터가 있는 칸의 좌표(x, y)와 바라보는 방향 direction 입력
x, y, direction = map(int, input().split())
visits[x][y] = 1 # 방문한 곳 저장하는 맵에 현재 캐릭터가 있는 좌표를 방문했다고 표시

# 전체 지도 입력
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    # direction 이 -1이 되는 경우 북:0, 동:1, 남:2, 서:3 중 서:3 으로 변경한다
    if direction == -1:
        direction = 3

# 캐릭터가 방문한 칸의 수를 카운트 하는 변수
# 1인 이유는? 캐릭터가 처음 위치한 칸을 방문했다고 처리하기 때문!
count = 1
# 캐릭터가 왼쪽 방향으로 회전한 경우( 이동하지 않고 왼쪽 방향으로 회전만 한 경우만 증가시킨다. )
turn_time = 0
# 시뮬레이션 시작
while True:
    # 왼쪽 방향으로 회전
    turn_left()
    next_x = x + dx[direction]
    next_y = y + dy[direction]
    # 현재 이동하려는 좌표가 방문한 적이 없고 바다가 아닌 경우
    if visits[next_x][next_y] == 0 and maps[next_x][next_y] == 0:
        # 방문했다고 표시
        visits[next_x][next_y] = 1
        # x, y 좌표 변경
        x = next_x
        y = next_y
        # 방문 카운트
        count += 1
        # 왼쪽 회전 횟수 0으로 초기화
        turn_time = 0
        # continue 제어문으로 아래 코드 실행하지 말고 while 반복문의 조건으로 이동
        continue
    # 현재 이동하려는 좌표로 이동할 수 없을 시
    else:
        # 왼쪽 방향으로 회전 횟수 증가
        turn_time += 1
    # 현재 캐릭터가 위치한 곳에서 네 방향 모두 방문한 곳이라면
    if turn_time == 4:
        # 바라보는 방향으로 뒤로 이동할 좌표 계산
        next_x = x - dx[direction]
        next_y = y - dy[direction]
        # 지도에서 뒤로 이동할 수 있는 곳이라면
        if maps[next_x][next_y] == 0:
            # 뒤로 이동
            # 방문한 곳들이기 때문에 방문 카운트를 하지 않는다
            x = next_x
            y = next_y
        # 지도에서 뒤로 이동할 수 없는 곳이다. 즉, 바다일 경우
        else:
            # 반복문 탈출
            break
        # 왼쪽 방향으로 회전 0으로 초기화
        turn_time = 0

# 방문한 곳 카운트 출력
print(count)