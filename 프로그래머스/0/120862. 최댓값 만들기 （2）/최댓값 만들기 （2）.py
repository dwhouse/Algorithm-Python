def solution(numbers):
    numbers.sort()
    if len(numbers) >= 4:
        a = numbers.pop()
        b = numbers.pop()
        c = numbers.pop(0)
        d = numbers.pop(0)
        return max(a*b, c*d)
    else:
        return numbers[-1]*numbers[-2]