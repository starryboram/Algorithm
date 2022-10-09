def solution(array, commands):
    a = []
    for i in range(len(commands)):
        s_array =  sorted(array[commands[i][0]-1:commands[i][1]])
        a.append(s_array[commands[i][2]-1])
    return a
