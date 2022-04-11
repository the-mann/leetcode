from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        most_freq = list(map(lambda x: x[0], sorted(count.items(), key=lambda x: x[1], reverse=True)))
        return most_freq[0:k]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
