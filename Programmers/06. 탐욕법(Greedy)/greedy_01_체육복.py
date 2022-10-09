# -*- coding: utf-8 -*-
def solution(n, lost, reserve):
    arr = [0] * n # 체육복 가지고 있는 학생 수 만큼 배열 생성

    for i in range(len(lost)): # 잃어버린애들 -1로 표시
        arr[(lost[i]-1)] = -1

    for j in range(len(reserve)): # 여유분 가지고 있는 애들 1로 표시
        arr[(reserve[j]-1)] = arr[(reserve[j]-1)] + 1

    for i in range(len(arr)-1):
        if (arr[i] == -1 and arr[i+1] == 1) or (arr[i] == 1 and arr[i+1]== -1):
            arr[i] = 0
            arr[i+1] = 0
            
    cnt = 0
    for j in range(len(arr)): # arr배열에서 0보다 큰 애들은 체육복을 가지고 있는 것을 의미
        if arr[j] >= 0:
            cnt += 1
    
    return cnt


n = 10
lost = [1, 3, 5, 7]
reserve = [1, 3]
solution(n, lost, reserve) # 확인용