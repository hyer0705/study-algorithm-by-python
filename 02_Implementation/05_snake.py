# 2020-11-17(Tue)
# 이것이 취업을 위한 코딩 테스트다 with python
# Chapter 04. 구현

# Q11. 뱀 P.327
# link: https://www.acmicpc.net/problem/3190

# 내가 작성한 코드
# 책에 나온 테스트 케이스만 성공

# n: 보드의 크기 입력 (2 <= N <= 100)
n = int(input())
# 보드 초기화
board = [[0] * n for _ in range(n)]
# 뱀이 방문한 곳을 저장하는 보드 초기화
snake_visit = [[0] * n for _ in range(n)]
# 초기 뱀의 위치
x = 0
y = 0

curr_snake_coordinates = []
curr_snake_coordinates.append([x, y])

snake_visit[x][y] = 1 # 뱀이 처음에 서 있는 곳 방문했다고 표시

# k: 사과의 개수 ( 0 <= K <= 100 )
k = int(input())

# 사과의 위치 입력
if k > 0:
    for i in range(k):
        row, col = map(int, input().split())
        # 2 는 사과의 위치를 뜻함
        board[row - 1][col - 1] = 2

# l: 뱀의 방향 변환 횟수 ( 1 <= L <= 100 )
l = int(input())
# 뱀의 방향 변환 정보 입력
snake_moves = []
for i in range(l):
    # (t초, c 방향)
    t, c = input().split()
    snake_moves.append((int(t), c))

# 왼쪽으로 90도 회전, 오른쪽으로 90도 회전을 해주는 함수
def turn_90_degree(d):
    global direction
    # 파라미터로 받은 방향이 'L'인 경우 ( 왼쪽으로 90도 회전 )
    if d == 'L':
        direction -= 1
    # 파라미터로 받은 방향이 'D'인 경우 ( 오른쪽으로 90도 회전 )
    elif d == 'D':
        direction += 1

    # direction 이 dx, dy 의 index 영역을 벗어난 경우를 막기 위해
    if direction == -1:
        direction = 3
    elif direction == 4:
        direction = 0

# 초기에는 오른쪽(동쪽)으로 이동
direction = 1
# 북: 0, 동: 1, 남: 2, 서:3 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 뱀의 몸의 길이를 저장하는 변수
snake_len = 1
# 반복문을 아얘 빠져나가라는 flag
is_out = False
# 시간을 저장하는 변수
time = 0
# 시뮬레이션 시작
next_x = 0
next_y = 0

index = 0
# board 안으로 있는 경우에만 반복
while next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board):
    # 시간 경과
    time += 1
    # x초 까지 뱀 이동 저장
    second = snake_moves[index][0]
    # x초 지난 후 뱀 회전 방향을 저장
    d = snake_moves[index][1]

    next_x = int(x) + dx[direction]
    next_y = int(y) + dy[direction]
    # board 안으로 있는 경우 와 자신의 몸에 닿지 않았을 경우
    if next_x >= 0 and next_x < len(board) and next_y >= 0 and next_y < len(board):
        if snake_visit[next_x][next_y] != 1:
            # 사과가 있는 경우
            if board[next_x][next_y] == 2:
                snake_len += 1  # 뱀의 몸 길이 1 증가
                snake_visit[next_x][next_y] = 1
                curr_snake_coordinates.append([next_x, next_y])
            # 사과가 없는 경우
            else:
                snake_visit[next_x][next_y] = 1  # 뱀이 이동한 곳 1로 변경
                curr_snake_coordinates.append([next_x, next_y])
                # 뱀의 몸 길이 증가 없이 이동 했으므로 이전에 있던 곳 0으로 변경
                snake_visit[curr_snake_coordinates[0][0]][curr_snake_coordinates[0][1]] = 0
                del curr_snake_coordinates[0]
            # 현재 위치로 변경
            x = next_x
            y = next_y
        elif snake_visit[next_x][next_y] != 1:
            break
        else:
            break
    # board 바깥으로 간 경우
    else:
        break

    # 뱀의 이동 증가
    if second == time:
        # 회전
        turn_90_degree(d=d)
        if index < len(snake_moves) - 1:
            index += 1

print(time)