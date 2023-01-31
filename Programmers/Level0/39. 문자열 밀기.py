# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A,B):
    for cnt in range(len(A)):
        if A == B:
            return cnt
        A = A[-1] + A[:-1]
    return -1

# 블로그 다른 풀이1.
def solution(A,B):
    A, B = list(A), list(B)
    
    for cnt in range(len(A)):
        if A == B:
            return cnt
        
        A.insert(0,A.pop())
    
    return -1

# 다른 풀이 2
from collections import deque

def solution(A,B):
    A, B = deque(A), deque(B)
    
    for cnt in range(len(A)):
        if A == B:
            return cnt
        
        A.rotate()
    
    return -1

# 다른 풀이3
def solution(A,B):
    BB = B*2
    return BB.find(A)