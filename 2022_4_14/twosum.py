class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        m = {}
        for i, x in enumerate(nums):
            m[x] = i

        for i, x in enumerate(nums):
            if (target - x) not in m:
                continue

            y = m[target - x]
            if y == i:
                continue

            return [i, y]
