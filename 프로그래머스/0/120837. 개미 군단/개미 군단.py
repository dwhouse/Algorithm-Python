def solution(hp):
    j, b, i = 0, 0, 0
    j = hp // 5
    b = (hp % 5) // 3
    i = hp - (j * 5) - (b * 3)
    return j+b+i