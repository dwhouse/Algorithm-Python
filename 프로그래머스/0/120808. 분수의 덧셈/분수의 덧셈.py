import math
def solution(numer1, denom1, numer2, denom2):
    result = [numer1 * denom2 + numer2 * denom1, denom1 * denom2]
    gcd = math.gcd(result[0], result[1])
    result = [result[0]//gcd, result[1]//gcd]
    return result