class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        grid = [[0]*n for i in range(n)]
        i = 0
        j = 0
        l = n
        k = 1
        while l >= 0:
            # fill out k to the right
            for x in range(n-l, l):
                i = x
                grid[j][i] = k
                k += 1
            # decrement l
            # Go down l
            for x in range(n-l+1, l):
                j = x
                grid[j][i] = k
                k += 1
            l -= 1
            # Go left l
            for x in range(l-1, n-l-2, -1):
                i = x
                grid[j][i] = k
                k += 1
            # decrement l
            # go up l
            for x in range(l-1, n-l-1, -1):
                j = x
                grid[j][i] = k
                k += 1
        return grid
print(Solution().generateMatrix(2))