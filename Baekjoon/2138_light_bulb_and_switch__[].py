import sys

sys.setrecursionlimit(10 ** 6)


def solution():
    N = int(sys.stdin.readline().strip())
    bulbs = list(sys.stdin.readline().strip())
    quiz = sys.stdin.readline().strip()

    def switch(curr_bulbs, count):
        nonlocal quiz, N

        for i in range(N):
            if curr_bulbs[i] != quiz.__getitem__(i):
                count += 1
                for n in [-1, 0, 1]:
                    curr = i+n
                    if 0 <= curr < N:
                        curr_bulbs[curr] = str(1 - int(curr_bulbs[curr]))

            if ''.join(curr_bulbs) == quiz:
                return count
        return -1


    keep_first = switch(bulbs.copy(), 0)
    bulbs[0] = str(1 - int(bulbs[0]))
    change_first = switch(bulbs.copy(), 1)

    if keep_first < 0 and change_first < 0:
        ans = -1
    elif change_first < 0:
        ans = keep_first
    elif keep_first < 0:
        ans = change_first
    else:
        ans = min(keep_first, change_first)

    sys.stdout.write(f"{ans}")


solution()