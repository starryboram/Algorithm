# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/120869
def solution(spell, dic):
    cnt = 0
    answer = []
    spell2 = spell.copy()
    for i in dic:
        for j in range(len(i)):
            if i[j] in spell2:
                spell2.remove(i[j])
            else:
                cnt += 1
            
        if (len(spell2) == 0):
            answer.append(1)
        spell2 = spell.copy()
            
    if sum(answer) >= 1:
        return 1
    else:
        return 2

# 다른사람 풀이(난멍청했다)
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2

# 또다른사람
import itertools
def solution(spell, dic):
    return int(bool(list(set(map("".join, list(itertools.permutations(spell)))) & set(dic)))) or 2