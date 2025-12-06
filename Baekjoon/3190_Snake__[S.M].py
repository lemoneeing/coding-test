import sys

input = sys.stdin.readline

rotated_dirs = {
    'U': {'L': 'L', 'D': 'R'},
    'R': {'L': 'U', 'D': 'D'},
    'D': {'L': 'R', 'D': 'L'},
    'L': {'L': 'D', 'D': 'U'}
}
dirs = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}  # 전진 방향


def move(snake, curr_dir, board):
    margin = len(board)

    r = snake[0][0] + dirs[curr_dir][0]
    c = snake[0][1] + dirs[curr_dir][1]

    if not (0 <= r < margin) or not (0 <= c < margin):
        return False

    # 이동할 칸 = 빈 칸
    if board[r][c] == 0:
        # 머리 이동
        board[r][c] = 1
        snake.insert(0, (r, c))

        # 꼬리 이동
        board[snake[-1][0]][snake[-1][1]] = 0
        if len(snake) > 1:
            snake.pop()

    # 이동할 칸 = 뱀
    elif board[r][c] == 1:
        return False

    # 이동할 칸 = 사과
    elif board[r][c] == 2:
        board[r][c] = 1
        snake.insert(0, (r, c))

    return True


def solution():
    N = int(input().strip())
    board = [[0] * N for _ in range(N)]  # 보드 위 빈 칸 = 0    board[0][0] = 1 # 보드 위 뱀 = 1
    board[0][0] = 1

    apple_cnt = int(input().strip())
    for _ in range(apple_cnt):
        apple = list(map(int, input().strip().split()))
        board[apple[0] - 1][apple[1] - 1] = 2  # 보드 위 사과 = 2

    moving_cnt = int(input().strip())
    moving = []
    for _ in range(moving_cnt):
        moving.append(input().strip().split())

    snake = [(0, 0)]

    curr_dir = 'R'

    game_time = 0
    is_game_over = False
    for time, d_type in moving:
        turn = int(time) - game_time if int(time) - game_time > 0 else 0
        for _ in range(turn):
            game_time += 1

            if not move(snake, curr_dir, board):
                is_game_over = True
                break

        if is_game_over:
            break

        curr_dir = rotated_dirs[curr_dir][d_type]

    if is_game_over:
        print(game_time)
    else:
        while not is_game_over:
            game_time += 1

            if not move(snake, curr_dir, board):
                break

        print(game_time)


solution()
