# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 예제 4-2. 시각 P.113
# 내가 작성한 코드

# 정수 n 입력
n = int(input())

cnt = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            time = str(h) + str(m) + str(s)
            # in 연산자: 좌측에 있는 피연산자가 우측 컬렉션에 속하는지 확인하는 연산자
            if '3' in time:
                cnt += 1

print(cnt)