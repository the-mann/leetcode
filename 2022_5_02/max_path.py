# Definition for a binary tree node.
from typing import Optional, Union, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.best = None

    def maxPathSum(self, root: Optional[TreeNode]) -> Union[float, int]:
        # Base Case
        if root is None:
            return float('-inf')

        # l and r store maximum path sum going through left
        # and right child of root respectively
        l = self.maxPathSum(root.left)
        r = self.maxPathSum(root.right)

        # Max path for parent call of root. This path
        # must include at most one child of root
        max_single = max(max(l, r) + root.val, root.val)

        # Max top represents the sum when the node under
        # consideration is the root of the maxSum path and
        # no ancestor of root are there in max sum path
        max_top = max(max_single, l + r + root.val)

        # Static variable to store the changes
        # Store the maximum result
        self.best = max(self.best, max_top)

        return max_single
