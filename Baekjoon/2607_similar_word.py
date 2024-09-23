import sys

def solution():
    N = int(sys.stdin.readline())
    fSpellCnt = {}
    first = ''
    fLen = 0
    ans = 0

    for _ in range(N):
        w = list(sys.stdin.readline().strip())

        if _ == 0:
            first = w
            # fLen = len(first)
        #     for c in set(first):
        #         fSpellCnt[c] = first.count(c)
            continue
        #
        # # 길이 차가 1 이하인 경우만 고려
        # if abs(len(w) - fLen) <= 1:
        #     currW = list(w)
        #     currSpellCnt = {}
        #     for c in set(currW):
        #         currSpellCnt[c] = currW.count(c)
        #
        #     allowed = 0
        #     # 길이 짧은 쪽 구성 요소가 큰쪽에 포함 되어야 함. ex) ab -> a or abc
        #     if fLen != len(currW):
        #         longer = fSpellCnt if len(first) > len(currW) else currSpellCnt
        #         shorter = currSpellCnt if len(first) > len(currW) else fSpellCnt
        #         if all(map(lambda x: x in longer, shorter.keys())):
        #             ans += 1
        #
        #     # 길이 동일
        #     else:
        #         # 구성 요소 같을 경우: 각 요소의 사용 횟수 합의 차이가 2 이하일 때만 허용 ex) aabbccc -> abcbabc(o), abcbaca(o), abbbbcc(x)
        #         if currSpellCnt.keys() == fSpellCnt.keys():
        #             for ch, cnt in fSpellCnt.items():
        #                 allowed += abs(currSpellCnt[ch] - cnt)
        #             if allowed <= 2:
        #                 ans += 1
        #
        #         # 구성 요소 다를 경우: 각 요소의 사용 횟수 합의 차이가 1 이하일 때만 허용 ex) ababa -> babac
        #         else:
        #             # longer = fSpellCnt if len(fSpellCnt.keys()) > len(currSpellCnt.keys()) else currSpellCnt
        #             # shorter = currSpellCnt if len(fSpellCnt.keys()) > len(currSpellCnt.keys()) else fSpellCnt
        #             # for ch, cnt in longer.items():
        #             #     allowed += abs(shorter.get(ch, 0) - cnt)
        #             # if allowed <= 1:
        #             #     ans += 1
        #             if len(set(first) - set(currW)) == 1 or len(set(currW) - set(first)) == 1:
        #                 ans += 1
        #
        #     print(ans)

        # 왜 어렵게 풀고 있었던 거냐...
        diffCnt = 0
        for c in first:
            if c in w:
                w.remove(c)
            else:
                diffCnt += 1

        if diffCnt <= 1 and len(w) <= 1:
            ans += 1


    sys.stdout.write(f"{ans}")

solution()