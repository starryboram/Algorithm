def solution(emergency):
    arr = []
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)} 
    # emergency = [3, 76, 24]일 경우 -> reverse해서 [76, 24, 3]으로 바뀜.
    # return dict {"3":3,"24":2,"76":1} 형태로 나타나짐
    for x in emergency:
        arr.append(dict[x]) 
    return arr
    # x = 3 => dict[3] = 3
    # x = 76 => dict[76] = 1
    # x = 24 => dict[24] = 2
# [3, 1, 2] 도출