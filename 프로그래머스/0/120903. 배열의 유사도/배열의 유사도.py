def solution(s1, s2):
    c = 0
    for i in s1:
        if i in s2:
            c += 1
    return c