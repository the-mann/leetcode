# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        self.bestBoth = []
        self.bestBothv = 0
        self.bestOne = []
        self.bestOnev = 0
        self.pathFromBest = []
        self.pathFromBestv = 0


class Solution:
    def __init__(self):
        self.currBest = []

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.setBests(root)

        return max(root.bestBothv, root.bestOnev)

    def setBests(self, root):

        if root is None:
            return

        self.setBests(root.left)
        self.setBests(root.right)

        l = root.left if root.left else TreeNode(-9999999999, None, None)
        r = root.right if root.left else TreeNode(-999999999, None, None)


        root.bestBothv = l.bestOnev + root.val + r.bestOnev

        root.bestBothv = max(root.bestBothv, l.bestBothv, r.bestBothv)
        root.bestBoth += l.bestOne
        root.bestBoth.append(root.val)
        root.bestBoth += r.bestOne

        root.pathFromBest.append(root.val)
        root.pathFromBestv += root.val

        if root.pathFromBestv < 0:
            # path from best is still negative, don't change bestOne.
            root.pathFromBest.append(root.val)
        else:
            # If val makes pathFromBest positive, we want to now have this as our bestOne
            root.bestOne += root.pathFromBest
            root.bestOnev += root.pathFromBestv
            root.pathFromBest = []
            root.pathFromBestv = 0


root = TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(Solution().maxPathSum(root))