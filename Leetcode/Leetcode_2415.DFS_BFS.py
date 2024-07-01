import sys


# root = [-1]
# root.extend(list(map(int, sys.stdin.readline().split(','))))
#
# print(root)
#
# sum = 0
#
# for e in range(len(root)//2):
#     for i, n in enumerate(root):
#         if i == 0:
#             continue
#
#         if i == 2 ** e:
#             if e % 2 == 0:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# root = [-1]
# root.extend(list(map(int, sys.stdin.readline().split(','))))
root = list(map(int, sys.stdin.readline().split(',')))

# tree = [[] for _ in range(len(root))]
tree = []
for i in range(len(root)):
    # for _ in range(pow(2, i)):
    tree.append(root[i:pow(2, i)+1])

print(tree)
# for i, n in enumerate(root):
#     if i == 0:
#         continue
#
#     if i * 2 < len(root):
#         tree.append(TreeNode(n, i * 2, i * 2 + 1))
#     else:
#         tree.append(TreeNode(n, None, None))
#
# def dfs_reverse(node):
#

