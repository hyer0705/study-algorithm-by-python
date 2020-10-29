# 2020-10-29
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Appendix B 기타 알고리즘 - 에라토스테네스의 체
#   자연수 N까지 모든 소수를 찾을 때 사용
#
#   1. 2부터 N까지의 모든 자연수를 나열
#   2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
#   3. 남은 수 중에서 i의 배수를 모두 제거(i는 제거하지 않음!)
#   4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복

# 알고리즘만 보고 내가 직접 구현해 본 것!

# 에라토스테네스의 체 구현 함수
def sieve_of_eratosthenes(n):
    # 2부터 입력한 숫자 N까지 리스트에 저장
    nums = [1 + i for i in range(1, n)]
    # 리스트의 0번째부터 마지막까지 반복
    for i in range(len(nums)):
        # 제거할 숫자를 저장할 set
        remove_set = set()
        # 리스트의 i + 1 번째 부터 마지막까지 반복 
        for j in range(i + 1, len(nums)):
            # j번째에 있는 숫자가 i번째에 있는 숫자의 배수일 때
            if nums[j] % nums[i] == 0:
                # remove_set 집합에 넣는다
                remove_set.add(nums[j])
        # remove_set에 있는 요소를 리스트에서 제거
        nums = [i for i in nums if i not in remove_set]
    return nums

# 자연수 N 입력 받기
n = int(input("자연수 N을 입력하세요: "))
# sieve_of_eratosthenes 함수의 반환 값을 list 라는 변수에 저장
prime_nums = sieve_of_eratosthenes(n)
# 소수만 출력
print("입력한 N까지의 숫자들 중 소수만 출력: " + str(prime_nums))