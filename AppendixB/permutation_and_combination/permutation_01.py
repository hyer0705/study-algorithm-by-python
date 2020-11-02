# 2020-11-02
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 순열과 조합
# 순열? 서로 다른 n개에서 r개를 선태갛여 일렬로 나열하는 것
#   nPr = n!/(n-r)!

# 1부터 4까지의 수 중에서 2개를 뽑아 한 줄로 세우는 모든 경우를 구하는 코드

import itertools

data = [1, 2, 3, 4]
permutation_list = itertools.permutations(data, 2)

# 내가 작성한 코드
print(list(permutation_list))
print("-----------------------------------------")

# 책에 나온 코드
for x in itertools.permutations(data, 2):
    print(list(x))