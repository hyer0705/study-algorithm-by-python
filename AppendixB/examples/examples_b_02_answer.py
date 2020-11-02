# 2020-11-02
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 예제 B-2. 암호 만들기(P.486)
# 출처: https://www.acmicpc.net/problem/1759

# [입력조건]
#   1. 첫째 줄에 두 정수 L,C가 주어진다. (3 <= L <= C <= 15)
#   2. 다음 줄에는 C개의 문자들이 주어지며 공백으로 구분한다.
#   3. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# [출력조건]
#   1. 각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.

# ** 최소 한 개의 모음과 최소 두 개의 자음으로 구성되어 있어야한다.

# 책에 나온 코드

import itertools

# 입력
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
alphas = input().split(' ')
alphas.sort()

vowels = {'a', 'e', 'i', 'o', 'u'} # 5개의 모음 정의

# 길이가 l 인 모든 암호 조합을 확인
for passowrd in itertools.combinations(alphas, l):
    # 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    count = 0
    for i in passowrd:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and l - count >= 2:
        print(''.join(list(passowrd)))