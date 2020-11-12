# Q. 모험가 길드
# p. 311

n = int(input())
fear_data = list(map(int, input().split()))
fear_data.sort()

count = 0
result = 0

for fear in fear_data:
    count += 1
    if fear <= count:
        result += 1
        count = 0

print(result)