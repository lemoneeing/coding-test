import sys

def main():
    n = int(sys.stdin.readline())

    p = [-1 for _ in range(n+1)]
    p[3] = 1
    p[5] = 1

    for i in range(6, n+1):
        if p[i - 5] > 0 and p[i - 3] > 0:
            p[i] = min(p[i-5]+1, p[i - 3]+1)
        if p[i-5] > 0:
            p[i] = p[i - 5] + 1
        if p[i - 3] > 0:
            p[i] = p[i-3]+1

    sys.stdout.write(f"{p[n]}")

if __name__ == "__main__":
    main()
