# Q. 문자열 뒤집기
# p.313

s = input()

cnt_zero = 0 # 0으로 만드는 횟수
cnt_one = 0 # 1로 만드는 횟수

if s[0] == '0':
    cnt_one += 1
else:
    cnt_zero += 1

for i in range(1, len(s) - 1):
    if s[i] != s[i +1]:
        if s[i + 1] == '0':
            cnt_one += 1
        else:
            cnt_zero += 1

print(min(cnt_zero, cnt_one))