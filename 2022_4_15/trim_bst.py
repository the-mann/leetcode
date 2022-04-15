# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        if root is None:
            return None
        elif low > root.val:
            return self.trimBST(root.right, low, high)
        elif high < root.val:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root


x = Solution().trimBST(TreeNode(val=1, left=TreeNode(val=0), right=TreeNode(val=2)), 1, 2)
print(x)