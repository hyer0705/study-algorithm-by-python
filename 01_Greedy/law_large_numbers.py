# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 2. 큰 수의 법칙(P.92) - 내가 직접 푼 코드

# 입력
#   n: 배열의 크기, m: 숫자가 더해지는 횟수
#   k: 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없음
n, m, k = map(int, input().split())

# n개의 자연수
nums = list(map(int, input().split()))
# nums 리스트 내림차순 정렬
nums.sort(reverse=True)

# 연속으로 더해지는 숫자를 확인하기 위해
count = 0
# 큰 수의 법칙에 따라 더해진 답을 저장하는 변수
result_sum = 0

for _ in range(m):
    count += 1
    if count > k:
        result_sum += nums[1]
        count = 0
    else:
        result_sum += nums[0]

# 더해진 결과 값 출력
print(result_sum)