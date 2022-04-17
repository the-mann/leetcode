from typing import Tuple


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> Tuple[str, bool]:
        n = len(s)
        a = [[("", True,) for j in range(n)] for i in range(n)]

        for i in range(n):
            a[i][i] = s[i], False

        for L in range(2, n):
            for i in range(0, n - L):
                j = i + L
                for k in range(i, j):
                    left = a[i][k]
                    right = a[k + 1][j]

                    bad = False
                    # check crossover
                    for x in left[0]:
                        if left[1] or right[1]:
                            bad = True
                            break
                        elif x in right[0]:
                            bad = True

                    if bad:
                        m = max(left, right, key=lambda x: len(x[0]))[0]
                        a[i][j] = (m, True,) if len(m) > len(a[i][j][0]) else a[i][j]
                    else:
                        z = left[0] + right[0]
                        a[i][j] = (z, False,) if len(z) > len(a[i][j][0]) else a[i][j]
        return a[0][n - 1]


print(Solution().lengthOfLongestSubstring("abcabcbb"))
