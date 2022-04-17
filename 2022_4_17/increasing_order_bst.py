# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.nums = []
        self.recurse(root)

        while len(self.nums) > 1:
            x = self.nums.pop()
            last = len(self.nums) - 1
            self.nums[last].left = None
            self.nums[last].right = x
        return self.nums.pop()

    def recurse(self, root: TreeNode):
        if root is None:
            return

        left = root.left
        right = root.right
        root.left = None
        root.right = None

        self.recurse(left)
        self.nums.append(root) if root is not None else None
        self.recurse(right)