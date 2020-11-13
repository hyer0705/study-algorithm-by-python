# 시뮬레이션 유형

# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 예제 4-1 상하좌우 p.110

# 내가 작성한 코드

# 공간의 크기를 나타내는 n 입력 ( 1 <= N <= 100 )
n = int(input())
# 여행가 A가 이동할 계획서 내용 ( 1 <= 이동 횟수 <= 100 )
move_data = list(input().split())

# 결과를 저장할 변수
x = 1 # x좌표
y = 1 # y좌표

# 이동 계획서에 따라 움직이기
for move in move_data:
    if move == 'L':
        if x - 1 > 0:
            x -= 1
    elif move == 'R':
        if x + 1 < n:
            x += 1
    elif move == 'U':
        if y - 1 > 0:
            y -= 1
    elif move == 'D':
        if y + 1 < n:
            y += 1

print(y, x)