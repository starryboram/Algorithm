# s가 주어질 때 Z가 나오면 이전 숫자 지우기 + 최종 남은 숫자 합하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120853
# 예) s = "10 Z 20 Z" => return 0
# s = "-1 -2 -3 Z" => return -3
# s = "1 2 Z 3" => return 4

def solution(s):
    arr = []
    for i in s.split(" "):
        try:
            arr.append(int(i))
        except:
            arr.pop()
    return sum(arr)

# 다른 사람 풀이
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer