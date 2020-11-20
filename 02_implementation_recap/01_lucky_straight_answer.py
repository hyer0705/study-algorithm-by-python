# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# Q07. 럭키 스트레이트 - 정답 코드 P.515

n = input()
half_length = len(n) // 2
summary = 0

for i in range(half_length):
    summary += int(n[i])

for i in range(half_length, len(n)):
    summary -= int(n[i])

print("LUCKY" if summary == 0 else "READY")