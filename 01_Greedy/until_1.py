# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 4. 1이 될 때까지 (P.99) - 내가 푼 코드

# n, k 입력
n, k = map(int, input().split())

count = 0

# 무한루프
while True:
    # n 이 1이 된 경우 반복문을 빠져나간다
    if n == 1:
        break
    # n이 k로 나누어 떨어질 때 나눈다
    if n % k == 0:
        n = n // k
    # n 이 k로 나누어 떨어지지 않는 경우 1을 뺀다
    else:
        n -= 1
    # 연산한 경우 count + 1
    count += 1

# 결과 출력
print(count)