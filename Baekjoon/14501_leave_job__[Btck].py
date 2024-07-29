import sys

def solution():
    N = int(sys.stdin.readline())
    cs = [None]
    for _ in range(N):
        cs.append(list(map(int, sys.stdin.readline().split())))

    def backtracking(n):
        nonlocal cs

        # n 이 N 보다 작고
        if n > N:
            return 0

        # n 번째 상담 소요시간이 N을 넘으면 그 상담은 무조건 제외
        if cs[n][0] + n - 1 > N:
            return backtracking(n+1)
        else:
            # n 을 선택할 때와 그렇지 선택하지 않을 경우 비교하여 반환
            return max(cs[n][1] + backtracking(n + cs[n][0]), backtracking(n + 1))

    sys.stdout.write(f"{backtracking(1)}")

solution()