def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            a = numbers[i] + numbers[j]
            if a not in answer:
                answer.append(a)
    answer.sort()
    return answer