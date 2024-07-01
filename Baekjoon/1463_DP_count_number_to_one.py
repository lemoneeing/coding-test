import sys

def main():
    # n = int(sys.stdin.readline())
    n = 100007
    mem = [sys.maxsize for _ in range(n+1)]
    mem[1] = 0
    if n > 1:
        mem[2] = 1
    if n > 2:
        mem[3] = 1

    if n > 3:
        for i in range(2, n+1):
            mem[i] = mem[i-1]+1
            if i % 3 is 0:
                mem[i] = min(mem[i], mem[i//3]+1)
            if i % 2 is 0:
                mem[i] = min(mem[i], mem[i//2] + 1)

    sys.stdout.write(f"{mem[n]}")

if __name__ == "__main__":
    import time

    start = time.time()
    main()
    sys.stdout.write(f"\n{time.time() - start}")