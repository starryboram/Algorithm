# 처음 풀이 -> 효율성에서 걸림
def solution(scoville, K):
    answer = 0
    while True:
        if min(scoville) >= K:
            return answer
        else:
            scoville.sort()
            scoville.append(scoville.pop(0) + (scoville.pop(0)*2))
            answer += 1
            if len(scoville) == 0:
                return -1
            elif len(scoville) == 1:
                if min(scoville) >= K:
                    return answer
                return -1

# heap 개념 도입 필요
# 리스트 원소 중에 min값을 하나하나 찾는 것은 시간 복잡도 측면에서 좋지 못함.
# 자동정렬되는 heap을 도입하여 리스트 [0] 원소 => min값임을 이용할 것.
# append = heappush!

# 수정된 풀이
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while True:
        if scoville[0] >= K:
            return answer
        else:
            heapq.heappush(scoville, (heapq.heappop(scoville) + (heapq.heappop(scoville)*2)))
            answer += 1
            if len(scoville) == 0:
                return -1
            elif len(scoville) == 1:
                if scoville[0] >= K:
                    return answer
                return -1

# 틈새 heap cheet
# arr = [1,3,5,2] -> heap list로 바꾸고 싶을 때 heapq.heapify(arr) / 힙 리스트를 h_list라 해보자
# min(arr) = h_list[0]
# arr.append(원소) = heapq.heappush(h_list, 원소)

# Rock_Kim 친절 풀이
from  heapq import heappop,heappush,heapify
def solution(scoville, K):
    ans = 0
    heapify(scoville)
    # 가장 작은 수 scoville[0] 
    # min(scoville) 을 쓰면 효율성에서 걸린다
    while scoville[0] < K:
        # 가장 작은 수와 그 다음 작은 수
        heappush(scoville,heappop(scoville) +(heappop(scoville)*2))
        ans += 1
        # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return ans