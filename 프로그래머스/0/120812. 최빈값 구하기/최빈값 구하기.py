def solution(array):
    f = [0 for i in range(1000)]
    for i in array:
        f[i] += 1
    m = max(f)
    if not f.count(m) == 1:
        return -1
    return f.index(m)