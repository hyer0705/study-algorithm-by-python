# 2020-11-10 (Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q04. 만들 수 없는 금액 - 정답 P.509

# 화폐단위를 오름차순 정렬 후 화폐 단위가 작은 동전부터 하나씩 확인하면서 target 변수를 업데이트하는 방법으로 최적의 해를 계산
# 1부터 target - 1 까지의 모든 금액을 만들 수 있는 상태

n = int(input())
coins = list(map(int, input().split()))
coins.sort() # 오른차순 정렬

target = 1

for coin in coins:
    if target < coin:
        break
    target += coin

print(target)