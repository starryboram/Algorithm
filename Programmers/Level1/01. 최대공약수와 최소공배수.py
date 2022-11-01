def solution(n, m):
    min_i = 0
    max_i = 0
    for i in range(min(n,m),0,-1):
        if n%i == 0 and m%i == 0:
            min_i = i
            break
        
    for i in range(max(n,m), (n*m)+1):
        if i%n == 0 and i%m == 0:
            max_i = i
            break
            
    return [min_i, max_i]