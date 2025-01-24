class Solution:
    def levelOrder(self, root) -> List[List[int]]:

        tree = []
        cnt = 0
        k = 1
        for i in range(len(root)):
            if i == 0:
                tree.append([root[i]])
            else:
                if cnt == 0:
                    tree.append([])
                if type(root[i]) is int:
                    tree[-1].append(root[i])

                cnt += 1
            if cnt == 2**k:
                k += 1
                cnt = 0

        return tree

print(Solution().levelOrder([3,9,20,'null','null',15,7]))