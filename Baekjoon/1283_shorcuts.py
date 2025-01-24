import sys
input = sys.stdin.readline
def solution():
    N = int(input().strip())
    shortcuts = {}
    for _ in range(N):
        option = input().strip()
        sc = []
        sc_subst = []
        prev_let = ' '
        for i, letter in enumerate(option):
            if letter != ' ':
                # 등록 안된 글자를 만나면 리스트에 위치 값과 함께 따로 저장
                if not (letter.lower() in shortcuts or letter.upper() in shortcuts):
                    if prev_let == ' ':
                        sc = (i, letter)
                        break
                    else:
                        sc_subst.append((i, letter))

            prev_let = letter

        if not sc and sc_subst:
            sc = sc_subst[0]

        if sc:
            shortcuts[sc[1]] = f"{option[:sc[0]]}[{sc[1]}]{option[sc[0] + 1:]}"
        else:
            shortcuts[option] = option

    for v in shortcuts.values():
        sys.stdout.write(f"{v}\n")

solution()