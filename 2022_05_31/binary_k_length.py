class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        x = set()
        z = set()
        # generate all binary codes of length k:
        for i in range(pow(2, k)):
            y = str(bin(i)).split("b")[1]
            y = ('0' * (k - len(y))) + y
            x.add(y)

        for i in range(0, len(s) - k + 1):
            z.add(s[i:(i + k)])
        return len(x) == len(z)

print(Solution().hasAllCodes("0101", 13))