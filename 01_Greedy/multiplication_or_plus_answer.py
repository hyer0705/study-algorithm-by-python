# 2020-11-04 (Wed)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q02. 곱하기 혹은 더하기 - 정답 P.507

# 두 수가 1 이하(0, 1) 인 경우 더하기 수행, 두 수가 2 이상인 경우 곱하기 수행

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)