# 2020-11-10 (Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q05. 볼링공 고르기 정답 P.512

# 무게마다 볼링공이 몇 개 있는지를 계산한 후 경우의 수를 계산한다.

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10 까지의 무게를 담을 수 있는 리스트
arr = [0] * 11

for ball_weight in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    arr[ball_weight] += 1

# 경우의 수를 담을 변수
result = 0
# 1 부터 m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    n -= arr[i]
    # B가 선택하는 경우의 수와 곱하기
    result += arr[i] * n

# 경우의 수 출력
print(result)