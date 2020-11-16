# 2020-11-16(Mon)
# 이것이 취업을 위한 코딩 테스트다 with python
# Chapter 04. 구현 문제

# Q07. 럭키 스트레이트 P.321
# link: https://www.acmicpc.net/problem/18406

# 내가 작성한 코드

# 점수 n 입력 (10 <= N <= 99,999,999 )
# 단, 점수 n의 자릿수는 항상 짝수 형태로만 주어짐!
n = input()

left_sum = 0
right_sum = 0

half = len(n) // 2 - 1

for i in range(half + 1):
    left_sum += int(n[i])
for i in range(half + 1, len(n)):
    right_sum += int(n[i])

print("LUCKY" if left_sum == right_sum else "READY")