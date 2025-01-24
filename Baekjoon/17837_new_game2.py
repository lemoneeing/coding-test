import sys
input = sys.stdin.readline

def move(token_num, all_token_info, curr_x, curr_y, color, next_x, next_y, board_stack):
    curr_tk = all_token_info[token_num]
    curr_stack = board_stack[curr_x][curr_y]

    curr_tk_height = curr_stack.index(token_num)
    move_tks = curr_stack[curr_tk_height:]
    if color == 1:
        move_tks.reverse()  # 빨간색으로 이동을 위한 역정렬

    board_stack[next_x][next_y].extend(move_tks)  # 기본 이동
    board_stack[curr_tk[0]][curr_tk[1]] = curr_stack[:curr_tk_height]  # 원래 칸 비우기

    # 이동한 모든 토큰들의 현재 위치 업뎃
    for stack_tk in move_tks:
        all_token_info[stack_tk][:2] = [next_x, next_y]


def solution():
    N, K = map(int, input().split())
    board = [[-1 for _ in range(N+2)]]
    tokens = [None]
    for _ in range(N):
        board.append([-1] + list(map(int, input().strip().split())) + [-1])
    board.append([-1 for _ in range(N+2)])

    tk_dir = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
    board_stack = [[[] for _ in range(N+2)] for __ in range(N+2)]

    # 게임 준비
    for tk in range(1, K+1):
        tokens.append(list(map(int, input().strip().split())))
        x, y = tokens[-1][:2]
        board_stack[x][y].append(tk)

    # 게임 시작
    for turn_cnt in range(1, 1001): # →, ←, ↑, ↓
        for t in range(1, K+1):
            curr_tk = tokens[t]
            c_x, c_y = curr_tk[:2]

            dir_idx = curr_tk[-1]
            n_x = c_x + tk_dir[dir_idx][0]
            n_y = c_y + tk_dir[dir_idx][1]

            dest = board[n_x][n_y]
            if 0 <= dest <= 1:
                move(t, tokens, c_x, c_y, dest, n_x, n_y, board_stack)

            elif dest == 2 or dest == -1: # 파란색이거나 막힌 곳: 역방향으로 이동
                # 방향 전환
                if dir_idx < 3:
                    new_dir_idx = tokens[t][-1] = 3 - dir_idx
                else:
                    new_dir_idx = tokens[t][-1] = 7 - dir_idx


                n_x = curr_tk[0] + tk_dir[new_dir_idx][0]
                n_y = curr_tk[1] + tk_dir[new_dir_idx][1]
                dest = board[n_x][n_y]

                # 파란색에 의해 바뀐 방향의 다음 칸 탐색
                if 0 <= dest <= 1:
                    move(t, tokens, c_x, c_y, dest, n_x, n_y, board_stack)

            if len(board_stack[n_x][n_y]) >= 4:
                sys.stdout.write(f"{turn_cnt}")
                return

    sys.stdout.write(f"-1")

solution()
