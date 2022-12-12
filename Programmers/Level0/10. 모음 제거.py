# a,e,i,o,u 들어갔을 경우에는 제거하고 공백 포함하여 리턴해주세요.
def solution(my_string):
    new_list = []
    for i in my_string:
        if (i != 'a') and (i != 'e') and (i != 'i') and (i != 'o') and (i != 'u'):
            new_list.append(i)
    return ''.join(str(s) for s in new_list)

# 다른 풀이(내꺼를 간추림)
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])


# 다른 풀이2
import re
def solution(my_string):
    return re.sub('[aeiou]', '', my_string)