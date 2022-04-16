# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.s = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Do postorder traversal, keep track of most recent sum
        self.postfix(root)
        return root

    def postfix(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        # else
        self.postfix(root.right)
        self.s += root.val
        root.val = self.s
        self.postfix(root.left)
        return 0