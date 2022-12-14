def solution(citations):
    citations = sorted(citations)
    
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]): # 논문 인용된 횟수 >= 인용된 논문 개수
            return len(citations[i:])
    return 0

# 다른 사람 풀이1
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
# 설명 : sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다. 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고, 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다. 
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다. 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.

# 다른 사람 풀이2
def solution(citations):
    citations.sort()
    n, answer = len(citations), 0
    for i, cites in enumerate(citations):
        h = n - i
        if cites >= h:
            return h
    return