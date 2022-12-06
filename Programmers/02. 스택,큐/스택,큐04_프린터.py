from collections import deque
def solution(priorities, location):
    queue = deque(priorities)
    cnt = 0
    if location == priorities.index(max(priorities)):
        return 1
    else:
        while len(queue):
            if location == 0: #몇 번째로 출력하는지 봐야하기 때문에 location이라는 조건을 걸어줌
                if queue[0] <max(queue):
                    queue.append(queue[0])
                    queue.popleft()
                    location = len(queue) - 1
                else:
                    return cnt + 1
 
            else:
                if queue[0] < max(queue):
                    queue.append(queue[0])
                    queue.popleft()
                    location -= 1
                else:
                    queue.popleft()
                    location -= 1
                    cnt += 1

# 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# 다른 사람 풀이2 
def solution(priorities, location):
    jobs = len(priorities)
    answer = 0
    cursor = 0
    while True:
        if max(priorities) == priorities[cursor%jobs]:
            priorities[cursor%jobs] = 0
            answer += 1
            if cursor%jobs == location:
                break
        cursor += 1   
    return answer