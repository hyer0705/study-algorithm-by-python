# 2020-10-29
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 투 포인터
# 리스트에 순차적으로 접근해야 할 때 2개의 점의 위치를 기록하면서 처리하는 알고리즘

# 정렬되어 있는 두 리스트의 합집합 구현 - 내가 직접 구현한 코드
#   1. 정렬된 리스트 A와 B를 입력받는다
#   2. 리스트 A에서 처리되지 않은 원소 중 가장 작은 원소를 i가 가리키도록 한다
#   3. 리스트 B에서 처리되지 않은 원소 중 가장 작은 원소를 j가 가리키도록 한다
#   4. A[i]와 B[j] 중에서 더 작은 원소를 결과 리스트에 담는다.
#   5. 리스트 A와 B에서 더 이상 처리할 원소가 없을 때까지 2~4번의 과정을 반복한다

data_a = [1, 3, 5, 7, 10, 11]
data_b = [2, 4, 6, 8]

merge_data = []

i = 0
j = 0

for index in range(len(data_a) + len(data_b)):
    if i == len(data_a) and j <= len(data_b):
        for k in range(j, len(data_b)):
            merge_data.append(data_b[k])
        break
    elif j == len(data_b) and i <= len(data_a):
        for k in range(i, len(data_a)):
            merge_data.append(data_a[k])
        break
    else:
        if data_a[i] > data_b[j]:
            merge_data.append(data_b[j])
            j += 1
        elif data_a[i] < data_b[j]:
            merge_data.append(data_a[i])
            i += 1

print(merge_data)