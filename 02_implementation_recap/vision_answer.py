# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter 04. 구현

# 예제 4-2. 시각 - 정답 코드 P.114

h = int(input())

cnt = 0
for hour in range(h + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(hour) + str(m) + str(s):
                cnt += 1

print(cnt)