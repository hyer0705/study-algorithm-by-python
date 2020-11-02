# 2020-11-02
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 구간 합 문제
# 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제

# 해결방법 1. 접두사 합
#   N개의 수에 대하여 접두사 합(Prefix Sum) 을 계산하여 배열 P에 저장한다
#   매 M개의 쿼리 정보 [L,R]을 확인할 때, P[R] - P[L-1]이다

# 내가 작성한 코드

# 접두사 합 계산 함수
def prefix_sum(data):
    # 파라미터로 넘겨받은 리스트를 기준으로 리스트 초기화
    prefix_list = [0] * (len(data) + 1)
    for i in range(1, len(prefix_list)):
        prefix_list[i] = prefix_list[i - 1] + data[i - 1]
    return prefix_list

# 구간합 계산 함수
def section_sum(left, right, prefix_list):
    return prefix_list[right] - prefix_list[left - 1]

# 예시 데이터(리스트)
data = [10, 20, 30, 40, 50]

# 접두사 합 리스트 초기화
prefix_list = prefix_sum(data)

# P.483 에 나온 예시들 확인하기
# 1. [1,3] 의 구간 합 구하기
print(section_sum(1, 3, prefix_list))
# 2. [2, 5] 의 구간 합 구하기
print(section_sum(2, 5, prefix_list))
# 3. [3, 4] 의 구간 합 구하기
print(section_sum(3, 4, prefix_list))