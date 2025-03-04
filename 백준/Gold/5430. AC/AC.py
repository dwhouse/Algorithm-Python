import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    result = []
    p = input() # R(배열 순서 뒤집기) D(첫 수 버리기) / 빈 배열 -> D : error
    n = int(input()) # 배열 길이
    arr = input().rstrip()# 배열 문자열 -> 실제 리스트로 변환
    
    if n == 0:
        dq = deque()
    else:
        newarr = arr[1:-1]
        #print(newarr)
        arr = list(map(int, newarr.split(",")))
        dq = deque(arr)

    rf = False
    ef = False
    
    for f in p:
        if f == "R":
            rf = not rf
        elif f == "D":
            if dq:
                if not rf:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print("error")
                ef = True
                break

    if not ef:
        if rf:
            dq.reverse()
        print("["+",".join(map(str, dq))+"]")
    
