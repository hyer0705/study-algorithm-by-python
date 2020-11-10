# 2020-11-10 (Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q03. 문자열 뒤집기 - 정답 P.508

# 모두 0으로 바꿀 때의 횟수와 1로 바꿀 때의 횟수를 계산하여
#   둘 중에 더 적은 횟수를 알아낸다.

s = input()

# 전부 0으로 바꾸는 경우
count0 = 0
# 전부 1로 바꾸는 경우
count1 = 0

# 첫 번째 원소에 대해서 처리
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(s) - 1):
    if s[i] != s[i+1]:
        if s[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))