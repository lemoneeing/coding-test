import sys

input = sys.stdin.readline


def solution():
    pw = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    continuous_vowels = ['aaa', 'eee', 'iii', 'ooo', 'uuu']
    consonants = []
    while True:
        conditions = [True, True, True] # 3가지 조건 충족여부
        pw = input().strip()
        if pw.lower() == 'end':
            return

        j = 0
        k = 0

        # 모음 포함 여부
        first_cond = any([True for v in vowels if v in pw])  # 최대 100회(20 x 5) 순회
        conditions[0] = first_cond

        if conditions[0]:
            for i in range(len(pw)+1): # 최대 20회
                if i > 2: # 모음 또는 자음 연속 3개
                    three_pieces = pw[j:] if i == len(pw) else pw[j:i]
                    if ([True for v in vowels if v in three_pieces] == [True, True, True]) or not any([True for v in vowels if v in three_pieces]):
                        secd_cond = False
                        conditions[1] = secd_cond
                        break
                    j += 1

                if i > 1:
                    two_pieces = pw[k:] if i == len(pw) else pw[k:i]
                    comp = list(set(two_pieces))
                    if len(comp) == 1:
                        if comp[0] != 'e' and comp[0] != 'o':
                            third_cond = False
                            conditions[2] = third_cond
                            break
                    k+=1

        if all(conditions):
            sys.stdout.write(f"<{pw}> is acceptable.\n")
        else:
            sys.stdout.write(f"<{pw}> is not acceptable.\n")

solution()
