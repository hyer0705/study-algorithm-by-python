# 2020-11-20(FRI)
# 이것이 취업을 위한 코딩 테스트다 with 파이썬
# Chapter04. 구현

# 실전문제. 왕실의 나이트 - 정답 코드 P.116

input_data = input()
row = int(input_data[1])
col = ord(input_data[0]) - ord('a') + 1

# (row, col)
steps = [
    (-1, 2)
    , (1, 2)
    , (-1, -2)
    , (1, -2)
    , (-2, 1)
    , (-2, -1)
    , (2, 1)
    , (2, -1)
]

result = 0
for step in steps:
    nrow = row + step[0]
    ncol = col + step[1]
    if nrow > 0 and nrow <= 8 and ncol > 0 and ncol <= 8:
        result += 1

print(result)