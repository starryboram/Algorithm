# n과 가까운 수부터 정렬하기
# [1, 2, 3, 4, 5, 6] => n = 4 => [4, 5, 3, 6, 2, 1] 출력
# [10000,20,36,47,40,6,10,7000] => n = 30 => [36, 40, 20, 47, 10, 6, 7000, 10000] 출력
def solution(numlist, n):
    arr = [[abs(n-i), n-i, i] for i in numlist]
    return [i[2] for i in sorted(arr)]   


# 다른 사람 풀이
def solution(numlist, n):
    answer = sorted(numlist, key = lambda x : (abs(x-n), n-x))
    return answer

# answer = sorted(numlist,key = lambda x : (abs(x-n), n-x)) key에 요소를 리스트 혹은 튜플로 두 개 이상 줄 수 있다. 
# 이 경우 앞에 값이 같을 때 뒤의 값을 이용해서 나열한다. 
# 요소 하나이고 값이 같을 때는 먼저 처리된 수가 먼저 나열됨.(인덱스가 작은 거)