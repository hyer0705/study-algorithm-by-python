# 2020-11-04 (Wed)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q03. 문자열 뒤집기 P.313

# 내가 푼 코드

# 문자열 s 입력
s = input()

# 0이 반복되는 구간 카운트
zero_cnt = 0
# 1이 반복되는 구간 카운트
one_cnt = 0

# 현재 기준이 되는 숫자를 담는 변수, 초기에는 0과 1 아무 관계 없는 숫자로 초기화 한다
current_num = -1
# 문자열 s를 하나씩 비교하는 반복문
for num in s:
    # 현재 기준이 되는 숫자와 반복문에서 가리키는 숫자를 비교했을 때, 서로 다른 경우
    # 즉, 연속되는 구간이 바뀌는 경우
    if current_num != num:
        # 현재 기준이 되는 숫자를 변경
        current_num = num
        # 현재 기준이 되는 구간이 0일 때
        if int(current_num) == 0:
            zero_cnt += 1
        # 현재 기준이 되는 구간이 1일 때
        else:
            one_cnt += 1

# 결과 출력
print(min(zero_cnt, one_cnt))