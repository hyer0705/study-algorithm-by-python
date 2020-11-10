# 2020-11-06 (Fri)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q04. 만들 수 없는 금액 (P.314)

# 내가 푼 코드

# 동전의 개수를 나타내는 양의 정수 N 입력
n = int(input())
# 화폐 단위 입력
coins = list(map(int, input().split()))
# 화폐 단위 내림차순 정렬
coins.sort(reverse = True)

# 금액 1씩 증가
money = 1
# 화폐 단위임을 뜻하는 변수
is_coin = False
# 만들 수 없는 금액을 찾기 위한 반복문
while True:
    # 안쪽 반복문에서 사용할 현재 금액을 저장하는 변수
    curr_money = money
    # 현재 금액을 만들 수 있는 금액인지 판단하는 반복문
    for coin in coins:
        # coins 리스트에 money 가 있다면 for문 break
        if money in coins:
            # 화폐 단위를 뜻하는 변수에 True 저장
            is_coin = True
            break
        # 현재 금액과 화폐를 뺐을 때의 금액이 0보다 크거나 같을 때만 뺀다
        if curr_money - coin >= 0:
            curr_money -= coin
        # 현재 금액이 0보다 작거나 같을 때 for문 break
        if curr_money <= 0:
            break
    # coins 리스트에 없고 curr_money 가 0이 아닐 때
    #   -> 만들 수 없는 금액임을 뜻함!
    if (not is_coin) and (curr_money != 0):
        break
    # 금액을 1 증가 시킴
    money += 1
    # coins 리스트에 있는지 확인하기 위해 다시 False 로 바꿈
    is_coin = False

# 만들 수 없는 금액 출력
print(money)