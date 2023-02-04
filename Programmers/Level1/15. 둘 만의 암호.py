def solution(s, skip, index):
    answer = ""
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in skip:
        if i in alpha:
            alpha.remove(i)
    alpha = alpha * 3
    
    for i in s:
        answer += alpha[alpha.index(i) + index]
    return answer

# 다른 사람 풀이
from string import ascii_lowercase

def solution(s, skip, index):
    result = ''

    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    l = len(a_to_z)

    dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

    for i in s:
        result += a_to_z[(dic_alpha[i] + index) % l]

    return result


# 다른 사람 풀이2
def solution(s, skip, index):
    answer = ''
    arr = [chr(i) for i in range(97, 123) if chr(i) not in skip] * 10
    for i in s:
        answer += arr[arr.index(i) + index]
    return answer