import sys

def solution():
    tc = 0
    ans = []
    nP = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

    while (N := int(sys.stdin.readline().strip())) > 0:
        tc += 1
        cave = []
        path = []
        for _ in range(N):
            cave.append(list(map(int, sys.stdin.readline().strip().split())))
            path.append([sys.maxsize for _ in range(N)])

        # 자체 시도 풀이: 슬라이딩 윈도우 -> 실패
        # for r in range(0, N):
        #     for c in range(0, N):
        #         if r == 0 and c == 0:
        #             path[r][c] = cave[r][c]
        #             continue
        #
        #         if r == 0:
        #             path[r][c] = path[r][c - 1] + cave[r][c]
        #         elif c == 0:
        #             path[r][c] = path[r - 1][c] + cave[r][c]
        #         else:
        #             path[r][c] = min(path[r][c - 1], path[r - 1][c]) + cave[r][c]
        # ans.append(str(path[N - 1][N - 1]))

        # 참고 풀이: 다익스트라
        q = [(0, 0)]
        path[0][0] = cave[0][0]
        while q:
            cX, cY = q.pop(0)
            cCost = path[cX][cY]

            if cX == N-1 and cY == N-1:
                if len(ans) == tc:
                    ans[-1] = min(path[N-1][N-1], cCost)
                else:
                    ans.append(cCost)
                continue

            # 상, 우, 하, 좌 로 탐색하면서 (현재 위치 비용) + (다음 위치 비용) 이 '지금 기록된 (다음 위치 비용)' 보다 작을 경우 갱신
            for dX, dY in nP:
                if 0 <= (nX := cX + dX) < N and 0 <= (nY := cY + dY) < N:
                    if path[nX][nY] > (cCost + cave[nX][nY]):
                        path[nX][nY] = cCost + cave[nX][nY]
                        if not q or (q and q[-1] != (nX, nY)):
                            q.append((nX, nY))

    
    for i, a in enumerate(ans):
        sys.stdout.write(f"Problem {i+1}: {a}\n")
        
solution()