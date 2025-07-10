import sys
from typing import List, Optional

input = sys.stdin.readline
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

def make_tree(nums, start, end):
    if start >= end:
        return None

    mid = (start + end) // 2

    node = TreeNode(val=nums[mid])
    node.left = make_tree(nums, start, mid)
    node.right = make_tree(nums, mid + 1, end)

    return node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''

        :param nums:
        :return:
        '''
        root = make_tree(nums, 0, len(nums))
        return root

Solution().sortedArrayToBST([-10,-3,0,5,9])
