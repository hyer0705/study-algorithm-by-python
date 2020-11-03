# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 2. 큰 수의 법칙(P.92) - 책에 나온 코드

# 가장 큰 수와 두 번째로 큰 수를 더한 값이 반복되는 수열을 찾아 문제를 해결
# 반복되는 수열의 길이 = k + 1
# 가장 큰 수가 반복되는 횟수 = int(m / (k+1)) * k + m % (k+1)
# 가장 작은 수가 반복되는 횟수 = m - count

# n, m, k 입력
n, m, k = map(int, input().split())
# N개의 수를 입력받기
nums = list(map(int, input().split()))
# 입력 받은 수 정렬
nums.sort()

# 가장 큰 수 와 두 번째로 큰 수
first = nums[n - 1]
second = nums[n - 2]

# 정답을 저장하는 변수
result = 0

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k + m % (k+1)

result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result)