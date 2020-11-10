# 2020-11-10 (Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q01. 모험가 길드_정답 P.506

# 공포도를 오름차순으로 정렬시킨 후, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하여 문제를 해결한다

n = int(input())
data = list(map(int, input().split()))
data.sort() # 오름차순 정렬

# 총 그룹의 수
result = 0

# 현재 그룹에 포함된 모험가의 수
count = 0

# 공포도를 낮은 것부터 하나씩 확인하며
for i in data:
    # 현재 그룹에 해당 모험가를 포함시키기
    count += 1
    # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    if count >= i:
        # 총 그룹의 수 증가
        result += 1
        # 현재 그룹에 포함된 모험가의 수 초기화
        count = 0

# 총 그룹의 수 출력
print(result)