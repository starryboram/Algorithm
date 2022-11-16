def solution(s):
    s_list = []
    for i in s:
        if len(s_list) == 0:
            s_list.append(i)
        elif s_list[-1] == "(" and i == ")":
            s_list.pop()
        elif s_list[-1] == i:
            s_list.append(i)
    if len(s_list) == 0:
        return True
    else:
        return False

# 다른 사람의 풀이 1
def is_pair(s):
    open_cnt = 0
    for c in s:
        if c == '(':
            open_cnt += 1
        elif c == ')':
            open_cnt -= 1
            if open_cnt < 0:
                return False
    return open_cnt == 0

# 다른 사람의 풀이 2 ---- 고수다...........
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0