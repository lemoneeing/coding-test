import sys
from collections import deque
        # 우      하      대
DIR = [(0, 1), (1, 0), (1, 1)]
ROT = [(0, 1), (1, 0), (1, 1)]

'''
pipe = [(head), (tail)]

우 밀 우 회
- 세로: pipe[0] + [0, 1] DIR[0]
- 대각: 
'''

def solve():
    N = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(N)]



solve()