# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
# n =  1234 => 1+2+3+4 = 10 return

def solution(n):
    answer = 0
    while True:
        if n <= 0: # 코드 구현하고 느낀거지만, n<=0조건을 굳이 안써도 되는....
            return answer
        else:
            answer += n%10
        n = n//10


# 다른 사람 풀이
def solution(n):
    return sum(list(map(int,list(str(n)))))

# 다른 사람 풀이2
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer