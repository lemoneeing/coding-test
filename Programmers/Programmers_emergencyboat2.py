def solution(people, limit):
    people.sort()
    crit = limit / 2

    # s_w = []
    # h_w = []
    # for w in people:
    #     if w <= crit:
    #         s_w.append(w)
    #     else:
    #         h_w.append(w)

    boat = 0
    si = sm = 0
    ei = em = len(people) - 1
    while si < ei:
        sw = people[0]
        hw = people[ei]

        if sw + hw <= limit:
            boat += 1
            si += 1
            sm = si
            ei -= 1
            em = ei
        else:
            ei -= 1

        if people[ei] <= crit:
            ei = em

    # if s_w:
    #     if len(s_w) % 2 == 0:
    #         boat += int(len(s_w) / 2)
    #     else:
    #         boat += (int(len(s_w) / 2) + 1)
    #
    # if h_w:
    #     boat += len(h_w)
    boat += people[sm:em+1]
    return boat

print(solution([70, 50, 80, 50], 100))