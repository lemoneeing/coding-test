import sys
import time


def fibo_top_down(n):

    if mem[n] >= 0:
        return mem[n]

    return fibo_top_down(n - 1) + fibo_top_down(n - 2)

def fibo_bottom_up(n):
    mem = [-1 for _ in range(n + 1)]
    mem[0] = 0
    mem[1] = 1

    for i in range(2, n+1):
        mem[i] = mem[i-1] + mem[i-2]

    return mem[n]


def main(type):
    # n = int(sys.stdin.readline())
    n = 45
    if type == "topdown":
        # top down 방식
        mem = [-1 for _ in range(n + 1)]
        mem[0] = 0
        mem[1] = 1

        sys.stdout.write(f"{fibo_top_down(n, mem)}")
    
    #down up 방식
    else:
        sys.stdout.write(f"{fibo_bottom_up(n)}")


if __name__ == "__main__":
    startTime = time.time()
    main("topdown")
    # main("bottomup")
    sys.stdout.write(f"\n{time.time() - startTime}")

