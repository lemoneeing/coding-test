import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = sys.stdin.readline().strip().split(',')
tree = []
right = TreeNode(root[2], None, None)
left = TreeNode(root[1], None, None)
head = TreeNode(int(root[0]), left, right)
tree.extend([head, left, right])
curr = 1
for i, n in enumerate(root[3:]):
    if n != "null":
        tree[curr*2].left = n
    else:?
        if i * 2
    node = TreeNode(int(n), len(tree))

visited = [False for _ in root]

root = sys.stdin.readline().strip().replace('null', '0').split(',')
sum = 0

def to_complete(arr):
    complete_bin_arr = [0, int(arr[0]), -1, -1]

    parent = 1
    for i, n in enumerate(arr):
        if i < 1:
            continue
        complete_bin_arr.extend([-1 for _ in range(parent * 2 + 1)])

        if n == 0:
            complete_bin_arr[parent * 2] = 0
            complete_bin_arr[parent * -1] = 0

        if complete_bin_arr[parent * 2] == -1:
            complete_bin_arr[parent * 2] = int(n)
        elif complete_bin_arr[parent * 2 + 1] == -1:
            complete_bin_arr[parent * 2 + 1] = int(n)
        else:
            p



    return complete_bin_arr

print(to_complete(root)[1:])

# def dfs(parent, left, right):
#     global root, sum
#
#     if right > len(root) and left > len(root):
#         sum += root[parent]
#         return
#
#     elif root[right] == -1 and root[left] == -1:
#         sum += root[parent]
#         return
#
#     if left < len(root) and root[left] > -1:
#         dfs(left, left * 2, left * 2 + 1)
#     if right < len(root) and root[right] > -1:
#         dfs(right, right * 2, right * 2 + 1)
#
# dfs(1, 2, 3)
# print(sum)


