def solution(strings, n):
    strings.sort() 
    return sorted(strings, key=lambda x:x[n])

######################################### lambda를 이용한 리스트 정렬 #########################################
s = ['5 A', '1 B', '4 C', '1 A']
sorted(s, key=lambda x: (x.split()[1], x.split()[0]))
# 출력: ['1 A', '2 A', '1 B', '4 C']

a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

sorted(a, key = lambda x : x[0]) # 출력: [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
sorted(a, key = lambda x : x[1]) # 출력: [(3, 0), (5, 1), (0, 1), (1, 2), (5, 2)]
sorted(a, key = lambda x : (x[0], -x[1])) # 출력: [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]
sorted(a, key = lambda x : -x[0]) # 출력: [(5, 1), (5, 2), (3, 0), (1, 2), (0, 1)]) # 참고) -x로 쓰면 역순으로 정렬해줌

################################ 조건식의 boolean 값이 True인 애들만 반환하기 ################################
a = [8, 4, 2, 5, 2, 7, 9, 11, 26, 13]
print(list(filter(lambda x : x > 7 and x < 15, a))) # 출력: [8, 9, 11, 13]

################################ reduce 이용(값 누적시키기) ################################
from functools import reduce 
t = [47, 11, 42, 13]
print(reduce(lambda x, y : x + y, t)) # 출력: 113

# 참고 사이트: https://gorokke.tistory.com/38
