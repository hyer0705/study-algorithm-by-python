# 2020-10-29
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘

# 특정한 합을 가지는 부분 연속 수열 찾기 문제
#   1. 시작점(start)과 끝점(end)이 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
#   2. 현재 부분합이 M과 같다면 카운트한다.
#   3. 현재 부분합이 M보다 작으면 end를 1 증가시킨다.
#   4. 현재 부분합이 M보다 크거나 같으면 start를 1 증가시킨다.
#   5. 모든 경우를 확인할 때까지 2부터 4번까지의 과정을 반복한다.

# 부분합이 5인 부분 연속 수열의 수는 몇 개인지 계산 - 내가 직접 구현한 코드

array = [1, 2, 3, 2, 5]
start = 0
end = 0
cnt = 0
M = 5

while start < len(array) and end < len(array):
    hop = 0
    if start == end:
        hop = array[start]
    else:
        for i in range(start, end + 1):
            hop += array[i]

    if hop == M:
        cnt += 1
        start += 1
    elif hop > M:
        start += 1
    else:
        end += 1

print(cnt)