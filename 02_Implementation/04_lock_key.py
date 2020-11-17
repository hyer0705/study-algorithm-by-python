# 2020-11-17(Tue)
# 이것이 취업을 위한 코딩테스트다 with Python
# Chapter 04. 구현

# Q10. 자물쇠와 열쇠 P.325
# link: https://programmers.co.kr/learn/courses/30/lessons/60059

# 내가 작성한 코드 + 정답 코드 본 후 구현
# 자물쇠 회전, 이동 구현은 했으나 답을 작성하지는 못함!

# 회전하는 함수 구현하기
def clock_wise_rotation(key):
    # key가 회전한 것을 저장하는 리스트
    change_key = [[0] * len(key) for i in range(len(key))]
    key_len = len(key) - 1
    # key 회전
    for row in range(len(key)):
        for col in range(len(key[row])):
            change_key[col][key_len] = key[row][col]
        key_len -= 1
    return change_key

# 상, 하, 좌, 우 이동하는 함수
# def move_key(key, direction):
#     # key가 이동한 것을 저장하는 리스트
#     change_key = [[0] * len(key) for i in range(len(key))]
#     # 상: 0, 하: 1, 좌: 2, 우: 3 / (row, col)
#     steps = [
#         (-1, 0)
#         , (1, 0)
#         , (0, -1)
#         , (0, 1)
#     ]
#
#     for row in range(len(key)):
#         for col in range(len(key[row])):
#             change_row = row + steps[direction][0]
#             change_col = col + steps[direction][1]
#             if change_row < len(key) and change_col < len(key):
#                 change_key[change_row][change_col] = key[row][col]
#
#     return change_key

# key 90도 회전
def rotate_90_degree(key):
    n = len(key) # key의 행 크기
    m = len(key[0]) # key의 열 크기
    new_key = [[0] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            new_key[col][n - row - 1] = key[row][col]
    return new_key

# 자물쇠와 key가 합이 맞는지 확인
def check(new_lock):
    lock_len = len(new_lock) // 3 # 원래 자물쇠의 길이
    for row in range(lock_len, lock_len * 2):
        for col in range(lock_len, lock_len * 2):
            # 1이 아닌 경우 합이 맞지 않는 경우가 있다면 False return
            if new_lock[row][col] != 1:
                return False
    # 모두 1인 경우 합이 맞는 경우! True return
    return True

def solution(key, lock):

    n = len(lock) # 자물쇠의 크기
    m = len(key) # 열쇠의 크기
    # 새 자물쇠 초기화
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새 자물쇠의 가운데에 원래 자물쇠 넣기
    for row in range(n):
        for col in range(n):
            new_lock[n + row][n + col] = lock[row][col]

    # 4번 회전시켜서 자물쇠에 맞는 열쇠인지 확인
    for direction in range(4):
        # 회전
        key = rotate_90_degree(key=key)
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 더하기
                for row in range(m):
                    for col in range(m):
                        new_lock[x + row][y + col] += key[row][col]
                        
                # 자물쇠와 열쇠의 합이 맞는 경우 True인 경우
                if check(new_lock=new_lock):
                    return True
                # 자물쇠에서 열쇠 빼기
                for row in range(m):
                    for col in range(m):
                        new_lock[x + row][y + col] -= key[row][col]

    return False

# 열쇠
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# 자물쇠
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key=key, lock=lock))