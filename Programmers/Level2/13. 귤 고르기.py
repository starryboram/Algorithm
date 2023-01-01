# 첫번째 풀이 - 시간 초과 6개
def solution(k, tangerine):
    set_tangerine = set(tangerine)
    answer = [tangerine.count(i) for i in set_tangerine]    
    answer = list(reversed(sorted(answer)))
    cnt = 0
    sum = 0

    if answer[0] >= k:
        return 1
    else:
        for i in answer:   
            sum += i
            cnt += 1
            if sum >= k:
                return cnt

# 두번째 풀이 - 또 통과 못함 ㅠㅠㅠㅠ
import heapq
def solution(k, tangerine):
    set_tangerine = set(tangerine)
    arr = []
    heapq.heapify(arr)
    for i in set_tangerine:
        heapq.heappush(arr, tangerine.count(i))
      
    cnt = 0
    sum = 0
    arr.sort()
    
    if arr[-1] >= k:
        return 1
    else:
        for i in arr[-1::-1]:   
            sum += i
            cnt += 1
            if sum >= k:
                return cnt 

# 새로운 방법 시도
# collections 의 Counter이라는 함수를 사용해보자.
from collections import Counter
def solution(k, tangerine):
    cnt = 0
    sum = 0
    for i in Counter(tangerine).most_common():
        sum += i[1]
        cnt += 1
        if sum >= k:
            return cnt

# Counter(배열).most_common() => 배열중에 최빈값을 튜플형태로 담아낸다.
# [1, 3, 2, 5, 4, 5, 2, 3] => [(3,2), (2,2), (5,2), (1,1), (4,1)]
# 튜플형태로 담아내기 때문에 최빈값을 더하기 위해서는 리스트 원소의 [1]값을 더해주면 됨.


# 다른 풀이
from collections import Counter
def solution(k, tangerine):
    total, count = 0, Counter(tangerine) # Counter(배열) : 얘는 dictionary 형태로 나타나짐!
    for index, each in enumerate(sorted(count.values(), reverse=True)):
        total += each
        if total >= k:
            return index + 1
    return k

# enumerate 잊지말자!