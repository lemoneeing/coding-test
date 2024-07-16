import sys


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = [i for i in range(n+1)]

    def find(n):
        nonlocal arr

        if arr[n] == n:
            return n

        arr[n] = find(arr[n])
        return arr[n]

    for _ in range(m):
        oper, n1, n2 = map(int, sys.stdin.readline().split())

        if oper == 0:
            # union 연산
            if n1 < n2:
                arr[n2] = find(n1) # 집합으로 연결
                # find(n1)
            else:
                arr[n1] = find(n2)
                # find(n1)

        else:
            if find(n1) == find(n2):
                sys.stdout.write(f"YES\n")
            else:
                sys.stdout.write(f"NO\n")

solution()