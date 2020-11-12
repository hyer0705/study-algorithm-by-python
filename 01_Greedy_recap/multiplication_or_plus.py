# Q. 곱하기 혹은 더하기
# p. 312

s = input()
result = 0

for i in s:
    now = int(i)
    if result <= 1 or now <= 1:
        result += now
    else:
        result *= now

print(result)