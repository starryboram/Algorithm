def solution(t, p):
    arr = [int(t[i:i+len(p)]) for i in range(len(t)-len(p)+1)]
    return len([i for i in arr if i <= int(p)])
