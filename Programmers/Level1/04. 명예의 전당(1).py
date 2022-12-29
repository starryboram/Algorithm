def solution(k, score):
    answer = [score[0]]
    arr = [score[0]]
    for i in score[1:]:
        arr.append(i)
        arr = list(reversed(sorted(arr)))
        if len(arr) > k:
            arr.pop(-1)
        answer.append(arr[-1])        
    return answer


# 다른 사람 풀이(heapq 이용)
import heapq

def solution(k, score):
    max_heap = []
    answer = []

    for sc in score:
        heapq.heappush(max_heap, (-sc, sc))
        answer.append(max(heapq.nsmallest(k, max_heap))[1])

    return answer