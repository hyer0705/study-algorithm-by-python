# 2020-11-19(THU)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q14. 외벽 점검 P.335
# link:https://programmers.co.kr/learn/courses/30/lessons/60062

# 내가 작성한 코드
# 어떻게 풀어야할지 모르겠다..!

# 순열 라이브러리 import
from itertools import permutations

# solution 함수
def solution(n, weak, dist):
    answer = len(dist) + 1 # 투입할 친구들의 최솟값을 담는 변수
    # 원형을 2배로 늘림
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
        
    # 원래 weak 리스트의 각 데이터들이 시작점으로 하여 계산
    for start in range(length):
        # dist 리스트의 순열(모든 경우의 수)
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 친구 수 카운트 변수
            position = weak[start] + friends[count - 1] # 시작점으로부터 현재 친구가 이동할 수 있는 거리 저장
            # 시작점부터 length(weak 리스트가 2배가 되기 전의 길이) 까지 반복
            for index in range(start, start + length):
                # 현재 취약점 > 현재 친구가 이동할 수 있는 거리 인 경우 ( 즉, 현재 친구가 고칠 수 없는 취약점! )
                if position < weak[index]:
                    count += 1 # 친구 증가
                    # dist의 길이(투입할 수 있는 친구) 보다 count 가 많아진 경우 반복문 종료
                    if count > len(dist):
                        break
                    # position 재설정
                    # position = 현재 취약점 + 방금 투입된 친구가 이동할 수 있는 거리
                    position = weak[index] + friends[count - 1]
            # 투입할 친구수의 최솟값 저장
            answer = min(answer, count)

    # answer(투입된 친구 수)가 dist 의 길이(투입될 수 있는 총 친구의 수) 보다 크다면
    # 모든 친구를 투입해도 전부 점검할 수 없으므로 return -1
    if answer > len(dist):
        return -1
    # answer return
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n=n, weak=weak, dist=dist))