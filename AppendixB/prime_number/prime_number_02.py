# 2020-10-29
# Appendix B 기타 알고리즘 - 소수의 판별
#   자연수 X의 소수 판별
#   자연수 X의 제곱근 까지만 나누어서 판별한다

# 내장함수 math 를 사용하기 위해 불러온다
import math

def is_prime_number(x):
    # 자연수 X를 2 부터 X의 제곱근 까지만 나누어 본다
    # 나누어지는 수가 있다면 그 수는 소수가 아니다
    for i in range(2, int(math.sqrt(x)) + 1): # math.sqrt(x) x의 제곱근을 반환한다
        if x % i == 0:
            return False # 소수가 아니다
        return True # 소수이다

print(is_prime_number(5))
print(is_prime_number(200))