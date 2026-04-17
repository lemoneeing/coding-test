import sys
input = sys.stdin.readline


def multiply_matrix(mat1, mat2, size):
    mult_res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            res = 0
            for k in range(size):
                res += mat1[i][k] * mat2[k][j]
            
            res %= 1000
            mult_res[i][j] = res
    
    return mult_res


def process_matrix_square(matrix, size, square):

    res = [[0] * size for _ in range(size)]
    for i in range(size):
        res[i][i] = 1

    while square > 0:
        if square % 2 == 1:
            res = multiply_matrix(res, matrix, size)
        
        matrix = multiply_matrix(matrix, matrix, size)
        
        square //= 2
    
    return res


def solve():
    N, B = map(int, input().split())
    mat_a = [list(map(int, input().split())) for _ in range(N)]

    ans = process_matrix_square(mat_a, N, B)
    for i in range(N):
        for j in range(N):
            sys.stdout.write(f"{ans[i][j]} ")
        sys.stdout.write(f"\n")


solve()