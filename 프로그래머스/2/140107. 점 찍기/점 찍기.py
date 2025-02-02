import math
def solution(k, d):
    c = 0
    for i in range(0, d+1, k):
        m_y = math.isqrt(d ** 2 - i ** 2)
        c += m_y//k + 1
    return c
        