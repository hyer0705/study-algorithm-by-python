# 2020-11-18(Wed)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q12. 기둥과 보 설치 P. 329
# link: https://programmers.co.kr/learn/courses/30/lessons/60061

# 내가 작성한 코드
# 문제 이해만 함...! -> 정답 코드를 참고하여 해결!

# 현재 구조물이 가능한 구조물인지 확인하는 함수
def is_possible(answer):
    for x, y, stuff in answer:
        # 기둥 규칙
        if stuff == 0:
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위' 인 경우만
            if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보 규칙
        elif stuff == 1:
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결' 인 경우만
            # 3, 2, 1
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False

    return True

# solution 함수
def solution(n, build_frame):
    answer = [] # 2차원 리스트로 반환

    # build_frame의 행 길이만큼 반복
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제 연산
        if operate == 0:
            answer.remove([x, y, stuff])
            if not is_possible(answer=answer):
                answer.append([x, y, stuff])
        # 설치 연산
        if operate == 1:
            answer.append([x, y, stuff])
            if not is_possible(answer=answer):
                answer.remove([x, y, stuff])

    return sorted(answer) # answer 리스트를 정렬한 후 return

n = 5 # 0: 바닥, 1~5까지 설치 가능!
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n=n, build_frame=build_frame))