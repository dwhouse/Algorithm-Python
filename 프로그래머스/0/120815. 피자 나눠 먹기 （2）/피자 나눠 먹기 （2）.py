import math
def solution(n):
    pizza = 0
    if n % 6 == 0:
        pizza = n // 6
    else:
        pizza = (n * 6 // math.gcd(n, 6)) // 6
    return pizza