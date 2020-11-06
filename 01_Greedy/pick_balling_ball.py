# 2020-11-06 (Fri)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q05. 볼링공 고르기(P.315)

# 내가 푼 코드

# combinations 를 사용하기 위한 라이브러리 import
import itertools

# n: 볼링공의 개수, m: 공의 최대 무게 입력
n, m = map(int, input().split())

# 각 볼링공의 무게 k 입력
k = list(map(int, input().split()))

# 두 사람이 볼링공을 고르는 경우의 수를 카운트하기 위한 변수
count = 0
# combinations 를 사용하여 두 사람이 볼링공을 고른 모든 경우의 수를 구하고 
# 서로 다른 볼링공을 고를 때만 카운트
for x in itertools.combinations(k, 2):
    # 첫 번째 사람이 고른 공의 무게
    first = x[0]
    # 두 번째 사람이 고른 공의 무게
    second = x[1]
    # 두 사람이 고른 공의 무게가 다를 때만 카운트
    if first != second:
        count += 1

# 경우의 수 출력
print(count)