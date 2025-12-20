import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution():
    M, N = map(int, input().split())
    star_ranks = []
    for _ in range(M):
        uv = list(map(int, input().split()))

        # 각 행성의 정렬 순서를 탐색하여 each_star_rank 로 기록
        tmp = []
        for star in uv:
            # bisect_left: 리스트에 있는 기존 요소 앞(왼쪽)에 오는 삽입 위치를 반환.
            tmp.append(str(bisect_left(uv, star)))
        star_ranks.append(' '.join(tmp)) # star_ranks = 각 우주의 행성 순위 리스트 모음

    ans = 0
    checked = []
    for i, rank_str in enumerate(star_ranks):
        if rank_str not in checked:
            rank_cnt = star_ranks.count(rank_str)
            if rank_cnt > 1:
                ans += int((rank_cnt ** 2 - rank_cnt) * 0.5)
            checked.append(rank_str)

    sys.stdout.write(f"{ans}")

solution()