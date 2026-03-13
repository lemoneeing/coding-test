import sys
input = sys.stdin.readline

def solve():
    # 입력 처리
    N, K = map(int, input().split())
    rects = []
    xs = set(); ys = set()

    for i in range(N):
        rect_input = list(map(int, input().split())) + [i+1]
        xs.add(rect_input[0]); xs.add(rect_input[2])
        ys.add(rect_input[1]); ys.add(rect_input[3])
        rects.append(rect_input)

    xs = sorted(list(xs))
    ys = sorted(list(ys))

    # 각 직사각형의 모서리 좌표 값(x / y)의 xs/ys에서의 인덱스를 map으로 정의
    x_map = {x: xi for xi, x in enumerate(xs)}
    y_map = {y: yi for yi, y in enumerate(ys)}

    
    # 좌표평면 각 칸을 직사각형 입력순서로 갱신
    grid = [[0] * (len(ys)+1) for _ in range(len(xs)+1)] # 주의: grid != 좌표평면, grid는 직사각형을 이루는 각 모서리칸을 xs, ys 상의 인덱스로 정리한 것
    for x1, y1, x2, y2, r_idx in rects:
        for x_idx in range(len(xs)):
            for y_idx in range(len(ys)):
                if grid[x_idx][y_idx] < r_idx: # 더 나중에 입력된 직사각형 번호로 갱신
                    grid[x_idx][y_idx] = r_idx

    # 면적 카운팅
    areas = {r: 0 for r in range(1, N+1)}
    for x_idx in range(1, len(xs)-1):
        for y_idx in range(1, len(ys)-1):
            r = grid[x_idx][y_idx]
            if r > 0:
                w = x_map[x_idx+1] - x_map[x_idx]
                h = y_map[y_idx+1] - y_map[y_idx]
                areas[r] += w*h

    tmps = []
    for i in range(1, N+1):
        tmps.append(areas[i], -i)
    tmps.sort(key=lambda x: (x[0], x[1]), reverse = True)

    ans = list(map(str, tmps[1:K+1]))

    sys.stdout.write('\n'.join(ans))


solve()