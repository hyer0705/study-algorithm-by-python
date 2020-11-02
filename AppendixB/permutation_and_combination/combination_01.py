# 2020-11-02
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 순열과 조합
# 조합? 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것을 의미
#   nCr = n!/r! * (n-r)!

# 1부터 4까지의 수 중에서 2개를 뽑는 경우를 구하는 코드

import itertools

data = [1, 2, 3, 4]
combi = itertools.combinations(data, 2)

# 내가 작성한 코드
print(list(combi))
print("------------------------------------")

# 책에 나온 코드
for x in itertools.combinations(data, 2):
    print(list(x), end = ' ')