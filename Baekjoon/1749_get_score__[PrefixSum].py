import sys

def solution():
    N, M = map(int, sys.stdin.readline().strip().split())
    matrix = []
    rPfxSum = [] # 행 단위로 누적 합
    cPfxSum = [] # 열 단위로 누적 합
    subPfxSum = [[0 for __ in range(M)] for _ in range(N)]  # 누적 합

    for r in range(N):
        matrix.append(list(map(int, sys.stdin.readline().strip().split())))

        rPfxSum.append([matrix[r][0]])
        cPfxSum.append([n for n in matrix[r]] if r == 0 else [])

        for c in range(M):
            if c > 0:
                rPfxSum[r].append(max(matrix[r][c], matrix[r][c] + rPfxSum[r][c-1]))

            if r > 0:
                cPfxSum[r].append(max(matrix[r][c], matrix[r][c] + cPfxSum[r - 1][c]))

    maxSubPfxSum = matrix[0][0]
    subPfxSum[0] = rPfxSum[0]
    for i in range(N):
        for j in range(M):

            if j == 0:
                subPfxSum[i][j] = cPfxSum[i][j]
                continue

            elif i > 0:
                subPfxSum[i][j] = matrix[i][j]

                for s in range(i):
                    subPfxSum[i][j] += rPfxSum[s][j]
                for e in range(j):
                    subPfxSum[i][j] += cPfxSum[i][e]

                if i > 0 and j > 0:
                    subPfxSum[i][j] -= subPfxSum[i-1][j-1]

            maxSubPfxSum = max(maxSubPfxSum, subPfxSum[i][j], rPfxSum[i][j], cPfxSum[i][j], matrix[i][j])

    sys.stdout.write(f"{maxSubPfxSum}")

solution()