MOD = 1000000007

def mat_mult(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                for j in range(n):
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

def mat_pow(A, power, n):
    # 단위행렬
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while power:
        if power & 1:
            result = mat_mult(result, A, n)
        A = mat_mult(A, A, n)
        power //=  2
    return result

def solve():
    import sys
    input = sys.stdin.readline

    T, N, D = map(int, input().split())
    
    maps = []
    for _ in range(T):
        Mi = int(input().strip())
        mat = [[0] * N for _ in range(N)]
        for _ in range(Mi):
            a, b, c = map(int, input().split())
            mat[a-1][b-1] = (mat[a-1][b-1] + c) % MOD
        maps.append(mat)
    
    if D == 0:
        for i in range(N):
            print(" ".join("1" if i==j else "0" for j in range(N)))
        return

    P = maps[0]
    for i in range(1, T):
        P = mat_mult(P, maps[i], N)

    L = D // T
    r = D % T

    P_exp = mat_pow(P, L, N)
    
    if r == 0:
        R = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
    else:
        R = maps[0]
        for i in range(1, r):
            R = mat_mult(R, maps[i], N)
    
    F = mat_mult(P_exp, R, N)
    
    for row in F:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    solve()
