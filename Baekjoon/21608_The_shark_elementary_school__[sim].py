import sys

def solution():
    N = int(sys.stdin.readline())
    students = {}
    cr = []
    points = [0]
    for i in range(1, N*N+1):
        ln = list(map(int, sys.stdin.readline().split()))
        students[ln[0]] = ln[1:]
        points.append(0)

        if i <= N:
            cr.append([-1] * N)

    # 자리 배치
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for student, friends in students.items():
        curr_pos = (sys.maxsize, sys.maxsize)
        mx_adjEmp = 0
        mx_adjFr = 0
        for j in range(N):
            for k in range(N):
                if cr[j][k] != -1:
                    continue

                # 현재 위치 기준으로 모든 인접 칸 탐색
                adj_emp = 0
                adj_fr = 0
                for idx, d in enumerate(dir):
                    if 0 <= j+d[0] < N and 0 <= k+d[1] < N:

                        # 인접 칸이 비어 있을 때 adj_emp + 1
                        if cr[j+d[0]][k+d[1]] == -1:
                            adj_emp += 1

                        # 인접 칸에 좋아하는 친구 adj_fr + 1
                        if cr[j+d[0]][k+d[1]] in friends:
                            adj_fr += 1

                # 좋아하는 친구가 많이 인접한 곳으로 자리 선정
                if mx_adjFr < adj_fr:
                    mx_adjFr = adj_fr
                    curr_pos = (j, k)
                    mx_adjEmp = adj_emp

                # 인접한 친구 수 같을 때
                elif mx_adjFr == adj_fr:
                    # 빈 인접 칸 수와 지금까지 탐색했던 빈 인접 칸 수의 최대 값이 다를 때 최대 값인 곳으로 자리 선정
                    if mx_adjEmp < adj_emp:
                        mx_adjEmp = adj_emp
                        mx_adjFr = adj_fr
                        curr_pos = (j, k)

                    # 빈 인접 칸 수가 최대치와 같을 때 좌표가 가장 낮은 곳으로 선정
                    elif mx_adjEmp == adj_emp:
                        if curr_pos[0] > j or curr_pos[0] == j and curr_pos[1] > k:
                            curr_pos = (j, k)

        cr[curr_pos[0]][curr_pos[1]] = student

    for r in range(N):
        for c in range(N):
            fCnt = 0
            curr_stud = cr[r][c]
            for p in dir:
                if 0 <= r+p[0] < N and 0 <= c+p[1] < N and cr[r+p[0]][c+p[1]] in students[curr_stud]:
                    fCnt += 1

            points[curr_stud] = 0 if fCnt == 0 else 10 ** (fCnt - 1)

    sys.stdout.write(f"{sum(points)}")

solution()