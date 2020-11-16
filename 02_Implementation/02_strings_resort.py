# 2020-11-16(Mon)
# 이것이 취업을 위한 코딩 테스트다 with python
# Chapter 04. 구현 문제

# Q08. 문자열 재정렬 P.322

# 문자열 S 입력
s = list(input())
s.sort() # 오름차순 정렬 -> 문자들의 순서 때문에

# 결과를 담을 리스트
result = []
# 숫자(0~9) 를 저장한 set
nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# 숫자들의 합을 저장할 변수
nums_sum = 0
# 입력받은 문자열 s 를 하나씩 비교하여 숫자를 찾아서 확인
for string in s:
    # 문자열이 nums set에 존재할 때! 즉, 숫자일 때
    if string in nums:
        # 더한다
        nums_sum += int(string)
    # 아니라면 result 리스트에 추가한다
    else:
        result.append(string)
# 반복문이 끝난 후 숫자들의 합을 리스트에 추가한다
result.append(str(nums_sum))

# 리스트를 하나씩 출력한다
for string in result:
    print(string, end='')