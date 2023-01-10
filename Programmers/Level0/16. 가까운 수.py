# 문제 풀이: array와 n이 주어졌을 때, n이랑 가장 가까운 수를 return 하기
# array = [3, 10, 28], n = 20일때 28 리턴
# 가까운 수가 여러개일 경우 더 작은 수 return

def solution(array, n):
    array.sort()
    dict = {abs(num-n):index for index, num in enumerate(array, start = 1)} # return dict {"17":12,"10":2,"8":3} / {"3":1,"2":2,"1":3}
    
    arr = [abs(i-n) for i in array]
    for i in range(len(arr)):
        if arr[i] == min(dict):
            return array[i]

# 다른 사람 풀이
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

# 다른 사람 풀이2
def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer