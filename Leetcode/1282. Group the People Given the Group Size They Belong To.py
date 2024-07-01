from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []

        # 순서대로 읽어서 값일단 같은 사이즈 별로 나눔.
        tmp = [[] for _ in range(len(groupSizes)+1)]
        for i, size in enumerate(groupSizes):
            tmp[size].append(i)

        for j, group in enumerate(tmp):
            if j == 0 or len(group) == 0:
                continue

            if len(group) > j:
                k = j
                while k <= len(group):
                    answer.append(group[k-j:k])
                    k += j
            else:
                answer.append(group)

        return answer

if __name__ == "__main__":
    s = Solution()
    s.groupThePeople([2,1,3,3,3,2])