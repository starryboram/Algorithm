def solution(p, c):
    if len(set(p)) != len(set(c)):
        return ''.join((set(p)- set(c)))
    
    else:
        for i in c:
            if c.count(i) != p.count(i):
                return i
