import sys
import heapq

input = sys.stdin.readline

def attack(scv_idx, damage_idx, turns):
    if all(map(lambda x: x >= 0, scv_list)):
        return turns



def solution():
    N = int(input())
    scv_list = list(map(int, input().split()))
    damages = [9, 3, 1]
    di = 0
    for i in range(N):
        scv_list[i] -= damages[di]


    sys.stdout.write(f"{ans}")

solution()
