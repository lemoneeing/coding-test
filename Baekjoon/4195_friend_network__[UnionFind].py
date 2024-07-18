import sys

def solution():
    nw = {}
    nw_counter = {}

    def find(person):
        nonlocal nw, nw_counter

        if person == nw[person]:
            return person

        nw[person] = find(nw[person])

        return nw[person]

    case = int(sys.stdin.readline())

    for _ in range(case):
        member = int(sys.stdin.readline())

        for __ in range(member):
            p1, p2 = sys.stdin.readline().split()
            if p1 not in nw:
                nw[p1] = p1
                nw_counter[p1] = 1
            if p2 not in nw:
                nw[p2] = p2
                nw_counter[p2] = 1

            p1 = find(p1)
            p2 = find(p2)
            if p2 == max(p1, p2):
                nw[p2] = p1
                nw_counter[p1] += nw_counter[p2]
                sys.stdout.write(f"{nw_counter[nw[p1]]}\n")
            else:
                nw[p1] = find(p2)
                nw_counter[p2] += nw_counter[p2]
                sys.stdout.write(f"{nw_counter[nw[p2]]}\n")

        nw.clear()
        nw_counter.clear()

    return

solution()