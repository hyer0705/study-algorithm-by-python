# 2020-11-04 (Wed)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q02. 곱하기 혹은 더하기 P.312

# 내가 푼 코드

# S 입력
s = input()

# 만들어질 수 있는 가장 큰 수를 저장하는 변수
result = 0

# 입력받은 문자열 S의 길이만큼 반복
for i in range(len(s)):
    # i 번째 문자가 0 또는 1일 경우, 현재 result 변수의 값이 0 또는 1일 경우 => 더하기
    if int(s[i]) <= 1 or result <= 1:
        result += int(s[i])
    # 곱하기 연산
    else:
        result *= int(s[i])

# 답변 출력
print(result)