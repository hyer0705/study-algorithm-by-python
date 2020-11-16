# 2020-11-16(Mon)
# 이것이 취업을 위한 코딩 테스트다 with python
# Chapter 4. 구현 문제

# Q09. 문자열 압축 P.323
# link: https://programmers.co.kr/learn/courses/30/lessons/60057

# 내가 작성한 코드

def solution(s):

    min_len = len(s)  # 문자열 압축된 것들 중에서 가장 길이가 짧은 것을 저장할 변수
    curr_len = 0 # 현재 단위로 문자열을 표현한 길이를 저장하는 변수
    # 문자열 s의 길이의 반 개 단위 까지만 반복되는지 확인한다
    for length in range(1, len(s) // 2 + 1):
        index = 0 # 현재 인덱스 0으로 초기화
        count = 0 # 얼마나 반복되는지 체크
        prev_str = s[index:index + length] # 이전에 비교한 문자
        result = "" # 문자열 압축이 저장될 변수

        # 현재 인덱스가 문자열의 길이보다 작거나 같을 때까지
        while index <= len(s):
            index += length # 현재 인덱스 계산
            curr_str = s[index:index + length] # 현재 인덱스에서 length 단위 만큼 자른 문자열
            if prev_str == curr_str: # 현재 문자열과 이전 문자열이 같을 경우
                count += 1 # 카운트 증가
            else: # 현재 문자열과 이전 문자열이 다를 경우
                if count > 0: # 카운트가 0보다 클 때
                    # 문자열 압축된 것 앞에 얼마나 반복됐는지 알려주면서 result에 붙인다.
                    result = result + str(count + 1) + prev_str
                else: # 카운트가 0일 때(반복되는 경우가 없음)
                    # 그냥 result에 붙인다
                    result = result + prev_str
                # 카운트 초기화
                count = 0
            prev_str = curr_str
        min_len = min(min_len, len(result))

    return min_len

s = "ababcdcdababcdcd"
# s = "aabbaccc"
print(solution(s=s))