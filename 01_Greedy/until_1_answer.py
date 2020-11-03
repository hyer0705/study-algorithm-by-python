# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 4. 1이 될 때까지 (P.99) - 책에 나온 코드

# n, k 입력
n, k = map(int, input().split())

result = 0

while True:
    # (N == K 로 나누어떨어지는 수)가 될 때까지 1 씩 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # N이 K보다 작을 때(더 잇아 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기ㅐㅣ.
result += (n - 1)
print(result)