# 2020-11-03(Tue)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part02 - Chapter03 Greedy

# 실전문제 3. 숫자 카드 게임(P.96) - 내가 푼 코드

# n, m 입력
n, m = map(int, input().split())
# 리스트 입력
number_card = []
for _ in range(n):
    number_card.append( list( map(int, input().split()) ) )

# 각 행에서 가장 작은 숫자 카드를 뽑아서 저장할 변수
result_card = -1

# 숫자 카드 게임 진행
for i in range(len(number_card)):
    # 선택된 행에서 가장 숫자가 낮은 카드를 뽑음
    current_card = min(number_card[i])
    # 현재 뽑은 카드가 결과 카드에 저장된 수보다 클 때 결과 카드 값을 현재 카드 값으로 변경
    if current_card > result_card:
        result_card = current_card

# 결과 출력
print(result_card)