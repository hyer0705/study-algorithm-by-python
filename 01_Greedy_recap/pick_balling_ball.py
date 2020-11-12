# Q. 볼링공 고르기
# p.315

# import itertools

n, m = map(int, input().split())
k_data = list(map(int, input().split()))

result = 0

# cnt = 0
#
# for x in itertools.combinations(k_data, 2):
#     if x[0] != x[1]:
#         cnt += 1
#
# print(cnt)

# 무게에 따른 볼링공 갯수 카운트
array = [0] * 11
for data in k_data:
    array[data] += 1

for i in range(1, m):
    n -= array[i]
    result += array[i] * n

print(result)