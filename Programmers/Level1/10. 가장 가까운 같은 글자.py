def solution(s):
    enu = {}
    answer = []
    for index, string in enumerate(s):
        answer.append(index-enu[string] if string in enu else -1)
        enu[string] = index
    return answer