class Solution(object):
    def __init__(self):
        self.m = 0
        self.n = 0

    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.m = len(grid)
        self.n = len(grid[0])
        x = []
        for row in grid:
            for num in row:
                x.append(num)
        for i in range(k):
            x.insert(0, x.pop())

        a = []
        for i in range(self.m):
            rowStart = (i * self.n)
            rowEnd = rowStart + self.n
            a.append(x[rowStart:rowEnd])
        return a


print(Solution().shiftGrid([[1], [2], [3], [4], [7], [6], [5]], 23))
