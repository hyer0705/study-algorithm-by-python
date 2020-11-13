# 완전탐색 유형

# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 예제 4-2 시각 p.113

# 내가 작성한 코드

# 정수 n 입력
n = int(input())

# 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서
#  3이 하나라도 포함되는 모든 경우의 수를 출력

# hour -> 0 ~ 23
# minute -> 0 ~ 59
# second -> 0 ~ 59
cnt = 0
for hour in range(n + 1):
    for minutes in range(60):
        for seconds in range(60):
            curr_time = str(hour) + str(minutes) + str(seconds)
            if '3' in curr_time:
                cnt += 1

print(cnt)