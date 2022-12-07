# 두 배열 중에 같은 원소의 개수만큼 리턴해주세요.
def solution(s1, s2):
    return len([i for i in s1 for j in s2 if i == j])

# 다른 사람의 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2))