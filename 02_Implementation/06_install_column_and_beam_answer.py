# 2020-11-18(Wed)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q12. 기둥과 보 설치 정답 코드 P.526
# 문제 link: https://programmers.co.kr/learn/courses/30/lessons/60061

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        # 설치된 것이 '기둥'인 경우
        if stuff == 0:
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 \
                    or [x-1, y, 1] in answer or [x, y, 1] in answer \
                    or [x, y-1, 0] in answer:
                continue
            # 아니라면 거짓(False) 반환
            return False
        # 설치된 것이 '보'인 경우
        elif stuff == 1:
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결' 라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer \
                    or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환

    return True

# solution 함수
def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame
        # 삭제 연산
        if operate == 0:
            answer.remove([x, y, stuff]) # 구조물을 일단 삭제
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        # 설치 연산
        if operate == 1:
            answer.append([x, y, stuff]) # 구조물을 일단 설치
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 삭제

    return sorted(answer)

n = 5 # 0: 바닥, 1~5까지 설치 가능!
build_frame = [
    [1,0,0,1]
    ,[1,1,1,1]
    ,[2,1,0,1]
    ,[2,2,1,1]
    ,[5,0,0,1]
    ,[5,1,0,1]
    ,[4,2,1,1]
    ,[3,2,1,1]
]
print(solution(n=n, build_frame=build_frame))