# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 실전 문제. 게임 개발 P.118

# 내가 작성한 코드

# n: 세로 크기, m: 가로 크기
n, m = map(int, input().split())
# (A, B): 게임 캐릭터가 있는 좌표, 바라보는 방향 d 입력
# 0: 북, 1: 동, 2: 남, 3: 서
x, y, d = map(int, input().split())
# 맵 입력, 0: 육지, 1: 바다
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# 캐릭터가 이동한 곳을 저장하는 맵
character_visit_map = [[0 for j in range(m) ] for i in range(n)]

# 방문한 곳은 1로 변경
# 캐릭터가 처음 위치한 곳은 방문한 곳으로 바꾼다
maps[x][y] = 1
character_visit_map[x][y] = 1
# 캐릭터가 방문한 곳 카운트
count = 1
# 캐릭터가 왼쪽방향으로 턴을 하는 함수
def turn_left():
    global d
    global turn_time

    turn_time += 1
    d -= 1
    if d == -1:
        d = 3
    return 0

turn_time = 0 # 캐릭터가 위치한 곳에서 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우를 가려내기 위한 변수
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# while True:
while True:
    # 캐릭터 왼쪽 방향으로 회전
    turn_left()
    # 다음에 갈 위치 계산
    next_x = x + dx[d]
    next_y = y + dy[d]
    # 입력받은 맵과 캐릭터가 방문한 것을 저장해둔 맵이 모두 방문한 적이 없을 경우에만 움직인다
    if maps[next_x][next_y] == 0 and character_visit_map[next_x][next_y] == 0:
        # 캐릭터 이동
        x = next_x
        y = next_y
        # 이동한 것 0으로 초기화
        turn_time = 0
        # 방문한 칸 카운트
        count += 1
        # 방문한 곳 1로 변경
        maps[x][y] = 1
        character_visit_map[x][y] = 1

    # 네 방향 모두 갈 수 없을 때
    if turn_time == 4:
        # 뒤가 바다일 경우 반복문 종료
        if maps[x - 1][y] == 1 and character_visit_map[x - 1][y] == 0:
            break
        # 한 칸 뒤로 가기
        x -= 1

print(count)