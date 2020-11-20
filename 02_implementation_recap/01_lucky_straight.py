# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q07. 럭키 스트레이트 P. 321
# 내가 작성한 코드

# 점수 N 입력
n = input()
half = len(n) // 2

left_sum = 0
right_sum = 0
for i in range(len(n)):
    if i < half:
        left_sum += int(n[i])
    else:
        right_sum += int(n[i])

print("LUCKY" if left_sum == right_sum else "READY")