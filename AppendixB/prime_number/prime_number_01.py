# 2020-10-29
# Appendix B 기타 알고리즘 - 소수의 판별
#   자연수 X의 소수 판별
#   2 부터 X - 1 까지 다 나누어 본다

def is_prime_number(x):
    # 파라미터로 넘겨 받은 x를 2부터 x - 1 까지 나누어본다
    # 하나라도 나누어지면 그 자연수는 소수가 아니다
    for i in range(2, x):
        if x % i == 0:
            return False # 소수가 아니다
        return True # 소수이다

print(is_prime_number(4))
print(is_prime_number(7))