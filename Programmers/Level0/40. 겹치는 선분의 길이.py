# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120876
def solution(lines):
    table = [set([]) for i in range(200)] #-100 to 100
    
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a, b):
            table[i + 100].add(index)
    
    count = 0
    for line in table:
        if len(line) > 1:
            count += 1
    
    return count # 생각이 안나서 블로그 참고 (다시 풀어보기)