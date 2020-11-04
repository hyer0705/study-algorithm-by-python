# 2020-11-04 (Wed)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q01. 모험가 길드 P.311

# 내가 푼 코드

# n 입력
n = int(input())
# 모험가의 공포도 입력
fears = list(map(int, input().split()))
# 공포도 리스트 정렬
fears.sort()

# 모험가 그룹 갯수 측정
count = 0
# fears 리스트의 인덱스를 뜻하는 변수
i = 0
# i 변수가 fears 리스트의 길이 값보다 작을 때까지 반복
while i < len(fears):
    # 인덱스 i에 위치한 fears 리스트의 값을 fear라는 변수에 저장
    fear = fears[i]
    # 모험가 그룹에 참여한 모험가의 수를 저장하는 변수
    adventure_cnt = 0
    # 안쪽 while 문에서 fears 리스트의 인덱스를 뜻하는 변수
    j = i
    # 인덱스 j가 fears 리스트의 길이보다 작을 때까지 반복
    while j < len(fears):
        # 현재 모험가 그룹에 참여한 모험가의 수가 현재 기준이 되는 공포도와 같을 때 count를 1 증가시키고 해당 반복문을 나간다(즉 모험가 모집 끝!)
        if adventure_cnt == fear:
            count += 1
            break
        # j 에 위치한 fears 리스트의 값이 현재 기준이 되는 공포도보다 작거나 같을 때, 모험가 그룹에 모험가 참여시킨다
        if fears[j] <= fear:
            adventure_cnt += 1
            # 모험가가 참여했으니 다음 반복문에 참여하지 않기 위해 바깥쪽 반복문의 인덱스를 뜻하는 i 값을 증가시킨다
            i += 1
        # 안쪽 반복문의 인덱스를 뜻하는 j 값을 증가시킨다(현재 기준이 되는 공포도와 비교한 값이므로!)
        j += 1

# 결과 출력
print(count)