def solution(n):
    n = str(n)
    s = []
    result = 0
    for i in n:
        s.append(i)
    for i in s:
        result += int(i)
    return result
        