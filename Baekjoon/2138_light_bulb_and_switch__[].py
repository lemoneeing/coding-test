import sys
sys.setrecursionlimit(10 ** 6)

def solution():
    N = int(sys.stdin.readline().strip())
    bulbs = list(sys.stdin.readline().strip())
    quiz = sys.stdin.readline().strip()
    neighbor = [-1, 0, 1]

    def bt(curr_bulbs, order, click):
        nonlocal quiz, N
        if ''.join(curr_bulbs) == quiz:
            return click

        elif order == N:
            return -1

        no_click = bt(curr_bulbs, order + 1, click)

        for n in neighbor:
            curr = order + n
            if 0 <= curr < N:
                curr_bulbs[curr] = str(1 - int(curr_bulbs[curr]))

        yes_click = bt(curr_bulbs, order + 1, click + 1)

        for n in neighbor:
            curr = order + n
            if 0 <= curr < N:
                curr_bulbs[curr] = str(1 - int(curr_bulbs[curr]))

        if no_click < 0 and yes_click < 0:
            return -1
        elif yes_click < 0:
            return no_click
        elif no_click < 0:
            return yes_click
        else:
            return min(no_click, yes_click)

    sys.stdout.write(f"{bt(bulbs.copy(), 0, 0)}")

solution()