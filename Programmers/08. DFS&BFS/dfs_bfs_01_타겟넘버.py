# -*- coding: utf-8 -*-
"""DFS/BFS_01. 타겟넘버.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E4ndz3YQ7Hl9uPJyfXcyUVFnQx6lqJos
"""

def solution(numbers, target):
    answer = 0
    arr = [0]
    for num in numbers:
        tmp = []
        for a in arr:
            tmp.append(a + num)
            tmp.append(a - num)
        arr = tmp
    
    for i in arr:
        if i == target:
            answer += 1
    return answer