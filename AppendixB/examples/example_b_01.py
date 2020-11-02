# 2020-11-02
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 예제 B-1 소수 구하기 (P.485)
# 출처: https://www.acmicpc.net/problem/1929

# M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# [입력조건]
#   첫째 줄에 자연수 M과 N이 빈칸을 사이에 두고 주어진다.(1 <= M <= N <= 1,000,000)
#   단, M 이상 N 이하의 소수가 하나 이상 있는 입력만 주어진다.

# [출력조건]
#   한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 에라토스테네스의 체 알고리즘을 사용하는 것이 어떨까?

import math

# m, n 입력
m, n = map(int, input().split())
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n) + 1)):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# m, n 까지 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)