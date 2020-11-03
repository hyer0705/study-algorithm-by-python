# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 예제 3-1. 거스름돈 P.87

change_money = 1260
# 큰 단위의 화폐부터 차례대로 확인
coins = [500, 100, 50, 10]

# 거스름돈 화폐 갯수
count = 0

for coin in coins:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += change_money // coin
    # 화폐로 거슬러 준 후 남은 돈
    change_money %= coin

print(count)