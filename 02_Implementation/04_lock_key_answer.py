# 2020-11-17(Tue)
# 이것이 취업을 위한 코딩테스트다 with python
# Chapter 04. 구현

# Q10. 자물쇠와 열쇠 정답 코드 P.518
# 정답 코드 따라 치면서 정리하기

# 2차원 리스트 90도 회전 함수
def rotate_a_matrix_by_90_degree(key):
    n = len(key) # 열쇠 행 길이 계산
    m = len(key[0]) # 열쇠 열 길이 계산
    # 일단 이렇게 쳐 보고 안되면 책에 있는 거로 바꾸기
    result = [[0] * m for _ in range(n)] # 결과 리스트
    for row in range(n):
        for col in range(m):
            result[col][n - row - 1] = key[row][col]
    return result # 90도 회전한 키 반환

# 자물쇠와 중간 부분이 모두 1인지 확인
def check(new_lock):
    # 자물쇠의 길이 = new_lock(열쇠와 자물쇠가 맞는지 확인하기 위해 자물쇠의 3배를 키운 자물쇠) // 3
    # 원래 자물쇠의 3배가 new_lock의 길이 이므로 3으로 나눈 몫을 원래 자물쇠(lock)의 길이이다
    lock_length = len(new_lock) // 3
    for row in range(lock_length, lock_length * 2):
        for col in range(lock_length, lock_length * 2):
            # new_lock이 1이 아닌 경우에는 합이 맞지 않다는 뜻! False를 return
            if new_lock[row][col] != 1:
                return False
    # new_lock의 lock 부분이 모두 1인 경우! 합이 맞다는 뜻! True를 return
    return True

def solution(key, lock):
    n = len(lock) # 자물쇠 크기
    m = len(key) # 열쇠 크기
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for row in range(n):
        for col in range(n):
            new_lock[row + n][col + n] = lock[row][col]
            
    # 4가지 방향에 대해서 확인, 한 번에 90도 회전
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key=key) # 열쇠 회전
        # new_lock의 x, y 좌표
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠를 끼워 넣기
                for row in range(m):
                    for col in range(m):
                        new_lock[x + row][y + col] += key[row][col]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock=new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for row in range(m):
                    for col in range(m):
                        new_lock[x + row][y + col] -= key[row][col]

    return False

# 열쇠
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# 자물쇠
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key=key, lock=lock))