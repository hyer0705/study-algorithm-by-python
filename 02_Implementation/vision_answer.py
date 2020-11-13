# 완전탐색 유형

# 2020-11-13 (Fri)
# 이것이 취업을 위한 코딩 테스트다 with Python
# Chapter 04. 구현

# 예제 4-2 시각 정답 코드 p.114

# n 입력받기
n = int(input())

cnt = 0
for hour in range(n + 1):
    for min in range(60):
        for sec in range(60):
            curr_time = str(hour) + str(min) + str(sec)
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in curr_time:
                cnt += 1

print(cnt)