# 처음 방식
import numpy as np
def solution(a, b):
    c = np.array(a) * np.array(b)
    return sum(c)
# 프로그래머스 미통과:
# TypeError: Object of type int64 is not JSON serializable


# 변경
import numpy as np
def solution(a, b):
    return int(sum(np.array(a) * np.array(b)))
# 프로그래머스 통과: int로 선언 해주면 됨

# numpy 안쓰는 방식
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])