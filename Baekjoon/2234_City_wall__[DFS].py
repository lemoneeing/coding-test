import sys

input = sys.stdin.readline


def solution():
    ans = ''
    N, M = map(int, input().split())
    city = []
    visited = [[0] * N for _ in range(M)]
    
    # 각 성곽의 위치를 이진수으로 치환: [남, 동, 북, 서]
    for _ in range(M):
        row = []
        for n in list(map(int, input().split())):
            row.append(list(map(int, list(format(n, '04b')))))

        city.append(row)

    room_cnt = 0
    room_size = [0]
    for row in range(M):
        for col in range(N):
            if visited[row][col] > 0:
                continue

            room_cnt += 1
            rsize = 0
            q = [(row, col)]
            while q:
                cr, cc = q.pop()
                if visited[cr][cc] > 0:
                    continue

                visited[cr][cc] = room_cnt
                rsize += 1
                for i, wall in enumerate(city[cr][cc]):
                    if wall == 0:
                        nr = cr
                        nc = cc
                        # 남
                        if i == 0:
                            if 0 <= cr+1 < N and not visited[cr+1][cc]:
                               nr += 1
                        # 동
                        elif i == 1:
                            if 0 <= cc+1 < N and not visited[cr][cc+1]:
                                nc += 1
                        # 북
                        elif i == 2:
                            if 0 <= cc-1 < N and not visited[cr][cc-1]:
                                nc -= 1
                        # 서
                        elif i == 3:
                            if 0 <= cr-1 < N and not visited[cr-1][cc]:
                                nr -= 1

                        q.append((nr, nc))

            room_size.append(rsize)

    for _ in range(M):
        print(visited[_])

solution()
