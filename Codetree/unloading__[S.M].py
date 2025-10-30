import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    garage = [[0] * (N+1) for _ in range(N+1)]
    loads = {}

    print("택배 투입")
    for _ in range(M):
        k, h, w, c = map(int, input().split())
        load = [h, w, c]

        stop = False
        for row in range(h, N+1):
            for col in range(c, c+w): # 택배의 너비만큼 순회
                # 이동할 칸이 빈 칸인지 체크
                if row <= N and garage[row][col] == 0:
                    continue
                else:
                    stop = True
                    row -= 1
                    break

            if row == N or stop:
                for rh in range(row, row-h, -1):
                    garage[rh][c:c+w] = [k] * w
                load.append(rh) # 현재 위치에서 정지
                break

        loads[k] = load

    for rw in range(N+1):
        print(f"{garage[rw]}")


    unloaded_cnt = 0
    while unloaded_cnt < M:
        print("택배 좌측 하차")
        # 하차할 택배 결정
        unloaded = 101
        for lid in loads.keys():
            l_h, l_w, l_c, l_r = loads[lid]
            if l_c == 1:
                unloaded = min(unloaded, lid)
            else:
                for col in range(l_c-1, 0, -1):
                    if garage[l_r][col] != 0:
                        break
                if col == 1 and garage[l_r][col] == 0:
                    unloaded = min(unloaded, lid)

        # 택배 하차
        print(unloaded)
        ul_h, ul_w, ul_c, ul_r = loads[unloaded]
        for ul_ri in range(ul_r, ul_r+ul_h):
            garage[ul_ri][ul_c:ul_c+ul_w] = [0] * ul_w
        unloaded_cnt += 1

        for rw in range(N+1):
            print(f"{garage[rw]}")

        print(f"택배 떨구기")
        for up_r in range(ul_r-1, 0, -1):
            if garage[up_r][ul_c] != 0:
                upl_id = garage[up_r][ul_c]
                upl_h, upl_w, upl_c, upl_r = loads[upl_id]
                if sum(garage[up_r+1][upl_c: upl_c + upl_w]) == 0:
                    for upl_ri in range(upl_r, upl_r+upl_h): # 지우고
                        garage[upl_ri][upl_c:upl_c+upl_w] = [0] * upl_w
                    for upl_rj in range(ul_r, ul_r-upl_h, -1):
                        garage[upl_rj][upl_c:upl_c+upl_w] = [upl_id] * upl_w
                    loads[upl_id][3] = ul_r-upl_h + 1
                else:
                    break

        for rw in range(N+1):
            print(f"{garage[rw]}")

        print("택배 우측 하차")
        # 하차할 택배 결정
        unloaded = 101
        for lid in loads.keys():
            l_h, l_w, l_c, l_r = loads[lid]
            if l_c + l_w - 1 == N:  # 오른쪽 끝 벽에 닿은 화물
                unloaded = min(unloaded, lid)
            else:
                for col in range(l_c + l_w, N + 1):
                    if garage[l_r][col] != 0:
                        break
                if col == N and garage[l_r][col] == 0:
                    unloaded = min(unloaded, lid)

        # 택배 하차
        print(unloaded)
        ul_h, ul_w, ul_c, ul_r = loads[unloaded]
        for ul_ri in range(ul_r, ul_r + ul_h):
            garage[ul_ri][ul_c:ul_c + ul_w] = [0] * ul_w
        unloaded_cnt += 1

        for rw in range(N + 1):
            print(f"{garage[rw]}")

        print("택배 떨구기")
        for up_r in range(ul_r - 1, 0, -1):
            if garage[up_r][ul_c] != 0:
                upl_id = garage[up_r][ul_c]
                upl_h, upl_w, upl_c, upl_r = loads[upl_id]
                # 밑 칸이 모두 비어있으면 아래로 낙하
                if sum(garage[up_r + 1][upl_c: upl_c + upl_w]) == 0:
                    for upl_ri in range(upl_r, upl_r + upl_h):
                        garage[upl_ri][upl_c:upl_c + upl_w] = [0] * upl_w
                    for upl_rj in range(ul_r, ul_r - upl_h, -1):
                        garage[upl_rj][upl_c:upl_c + upl_w] = [upl_id] * upl_w
                    loads[upl_id][3] = ul_r-upl_h + 1
                else:
                    break

        for rw in range(N + 1):
            print(f"{garage[rw]}")

solution()
