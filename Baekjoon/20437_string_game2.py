import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    T = int(input())
    for _ in range(T):
        W = input().strip()
        K = int(input())

        min_len = 0
        max_len = 0
        w_index = defaultdict(list)
        w_target = []

        for idx, ch in enumerate(W):
            if W.count(ch) >= K:
                w_index[ch].append(idx)
                if ch not in w_target:
                    w_target.append(ch)

        if not w_target:
            sys.stdout.write(f"-1")

        else:
            min_len = len(W)
            max_len = 0

            for ch in w_target:
                for i, curr_pos in enumerate(w_index[ch]):
                    if i+K > len(w_index[ch]):
                        break

                    cur_len = w_index[ch][i+K-1] - curr_pos + 1
                    min_len = min(min_len, cur_len)
                    max_len = max(max_len, cur_len)

            sys.stdout.write(f"{min_len} {max_len}")
        sys.stdout.write(f"\n")


def solution():
    T = int(input())
    for _ in range(T):
        W = input().strip()
        K = int(input())

        if K == 1:
            sys.stdout.write(f"1 1\n")
            continue

        min_l = len(W) + 1
        max_l = 0

        w_cnt = {}
        for idx, ch in enumerate(W):
            indexes = w_cnt.get(ch, [])
            if indexes:
                w_cnt[ch].append(idx)
            else:
                w_cnt.update({ch: [idx]})

        for w, idxs in w_cnt.items():
            if len(idxs) >= K:
                for i, s_idx in enumerate(idxs[:-K+1]):
                    curr_l = idxs[i + K - 1] + 1 - s_idx

                    min_l = min(min_l, curr_l)
                    max_l = max(max_l, curr_l)

        if min == len(W) + 1 or max_l == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(f"{min_l} {max_l}\n")

solution()