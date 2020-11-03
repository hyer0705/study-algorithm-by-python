# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 3. 숫자 카드 게임(P.96) - 책에 나온 코드

# n, m 입력
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for _ in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수' 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

# 최종 답안 출력
print(result)