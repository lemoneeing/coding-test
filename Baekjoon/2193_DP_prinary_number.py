import sys

def main():
    n = int(sys.stdin.readline())

    D = [[0, 0] for _ in range(n+1)]
    D[1] = [0, 1]

    for i in range(2, n+1):
        D[i] = [sum(D[i-1]), D[i-1][0]]

    sys.stdout.write(f"{sum(D[n])}")

if __name__ == "__main__":
    main()