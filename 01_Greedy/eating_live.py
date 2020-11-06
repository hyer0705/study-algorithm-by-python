# 2020-11-06 (Fri)
# 이것이 취업을 위한 코딩테스트다 with 파이썬
# Part03 - Chapter03 Greedy

# Q06. 무지의 먹방 라이브(P.316)

# 내가 푼 코드
#   채점 결과 효율성 0점... 정확성 한 문제 빼고 다 맞춤!

# solution 함수
def solution(food_times, k):
    # return 값
    answer = -1
    # 마지막에 먹은 음식의 인덱스를 저장
    index = 0
    # k 초 만큼 방송 진행
    while k > 0:
        # food_times의 길이만큼 반복
        for i in range(len(food_times)):
            # food_times 의 i번째 음식이 남아있을 때
            if food_times[i] > 0:
                # 음식 먹기
                food_times[i] -= 1
                # 먹방 라이브 시간이 1초씩 지나감
                k -= 1
            # k == 0 이 되면 for문 break
            if k <= 0:
                # k가 0이 되는 순간 index의 다음 index를 저장
                index = i + 1
                break

    # index 값이 리스트 food_times 의 길이와 같을 때
    if index == len(food_times):
        # index 값을 첫 번째 값으로 바꿔준다
        index = 0
    # index 부터 리스트의 끝까지 반복하여 남아 있는 음식  체크
    for i in range(index, len(food_times)):
        # 남아 있는 음식이 있으면 해당 음식의 위치 반환
        if food_times[i] > 0:
            answer = i + 1
            return answer

    # index 부터 리스트의 끝까지 반복하여 남아 있는 음식을 못찾았을 경우 
    # 첫 번째부터 index 까지 남아 있는 음식 체크
    if answer == -1:
        for i in range(0, index + 1):
            # 남아 있는 음식이 있으면 해당 음식의 위치 반환
            if food_times[i] > 0:
                answer = i + 1
                return answer

    # 남아 있는 음식이 없을 경우 -1 반환
    return answer

# food_times: 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열
# food_times = [4,2,3,6,7,1,5,8]
# food_times = [3, 1, 2]
food_times = [1, 1, 1, 1]
# food_times = [946, 314, 757, 322, 559, 647, 983, 482, 145]
# k: 방송이 중단된 시간
# k = 27
# k = 5
k = 4
# k = 1833

# 답 출력
print(solution(food_times=food_times, k=k))