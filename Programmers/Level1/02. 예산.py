def solution(d, budget):
    arr = []
    if sum(d) <= budget:
        return len(d)
    else:
        for i in sorted(d):
            arr.append(i)
            if sum(arr)> budget:
                return len(arr)-1