# quiz: ["3 - 4 = -3", "5 + 6 = 11"] => return ["X", "O"]
# quiz: ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"] => return ["O", "O", "X", "O"]
def solution(quiz):
    answer = []
    for i in quiz:
        if eval(i.replace("=","==")) == True:
            answer.append("O")
        else:
            answer.append("X")
    return answer

# 다른 사람의 풀이(split으로 좌항 우항을 비교)
def solution(quiz):
    answer = []
    for q in quiz:
        p, a = q.split("=")
        if eval(p) == int(a):
            answer.append("O")
        else:
            answer.append("X")
    return answer