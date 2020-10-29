# 투자 금액 입력 받기
investment = int(input())
# 투자 일 수
day = int(input())
# 변동 입력 받기
fluctuations = list(map(int, input().split()))

# 주식의 수익을 계산한 값
incoming = investment
for i in fluctuations:
    incoming *= (1 + (i * 0.01))

result = incoming - investment

# 순수익 출력
print("%.0f" % result)
# 수익에 대한 상태 출력
if result > -0.5 and result < 0.5:
    print("same")
elif result > 0:
    print("good")
elif result < 0:
    print("bad")