import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    houses = [tuple(map(int, input().split())) for _ in range(N)]
    houses.sort()

    pop_sum = 0
    prefix_pop = [(houses[i][0], pop_sum := pop_sum+houses[i][-1]) for i in range(N)]

    for town in prefix_pop:
        if town[1] >= pop_sum/2:
            print(town[0])
            return

solution()