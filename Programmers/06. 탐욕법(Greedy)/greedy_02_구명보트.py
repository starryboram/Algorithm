def solution(people, limit):
    s_people = sorted(people)
    answer = 0
    a = 0
    b = len(people)-1
    while a <= b:
        answer += 1
        if s_people[b] + s_people[a] <= limit:
            a += 1
        b -= 1
    return answer
