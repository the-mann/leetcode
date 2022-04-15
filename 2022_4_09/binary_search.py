class Solution(object):
    def __init__(self):
        self.nums = None
        self.target = None

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        self.nums = nums
        self.target = target

        return self.searchBetween(0, len(nums) - 1)

    def searchBetween(self, start, end):
        if end - start <= 1:
            if self.target not in [self.nums[start], self.nums[end]]:
                return -1

        mid = start + (end - start) // 2

        if self.target > self.nums[mid]:
            return self.searchBetween(mid + 1, end)
        elif self.target < self.nums[mid]:
            return self.searchBetween(start, mid)
        else:
            return mid


print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
