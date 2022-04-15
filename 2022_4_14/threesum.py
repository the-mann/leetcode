from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = {}
        n = set()
        primes = [1, 2, 3, 5, 7, 11, 13, 17]
        target = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j:
                    m[x + y] = i, j

        for k, z in enumerate(nums):
            if (target - z) not in m:
                continue

            i,j = m[target - z]
            if k != i and k != j:
                x = [nums[i], nums[j], nums[k]]
                x.sort()
                n.add(tuple(x))

        return list(list(x) for x in n)


print(Solution().threeSum([3,0,-2,-1,1,2]))