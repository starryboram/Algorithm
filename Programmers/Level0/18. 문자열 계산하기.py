# my_string = "3 + 4" 일때 7 return 하기
# + 혹은 - 만 주어짐

import re
def solution(my_string):
    arr = re.findall("\d+", my_string)
    brr = [i for i in my_string if (i == "+") or (i == "-")]
    cnt = int(arr[0])
    for i in range(len(brr)):
        if brr[i] == "+":
            cnt += int(arr[i+1])
        else:
            cnt -= int(arr[i+1])
    return cnt

# import re 처음에 풀었다가 실패함
# def solution(my_string):
#     arr = re.findall("\d+", my_string)
#     a = my_string.count("+")
#     arr = [int(i) for i in arr]
#     return sum(arr[:a+1]) - sum(arr[a+1:])

# 다른사람 풀이
solution=eval #!!!!!!!!!!!!!!!?????????????...............현타
# eval은 그냥 문자열 그대로 계산해주는 걸 말함. ㅋ




