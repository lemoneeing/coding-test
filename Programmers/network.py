def solution(n, computers):

    union = [_ for _ in range(n)]

    def find(idx):
        if idx == union[idx]:
            return idx

        union[idx] = find(union[idx])

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                curr = i if i > j else j
                head = j if curr == i else i
                union[curr] = head
                find(curr)

    return len(set(union))


print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))