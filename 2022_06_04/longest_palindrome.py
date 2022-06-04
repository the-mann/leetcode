class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        x = len(s)
        for i in range(x):
            left = i
            right = i
            while left >= 0 and right < x and s[left] == s[right]:
                if right - left >= len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1

            left = i
            right = i + 1
            while left >= 0 and right < x and s[left] == s[right]:
                if right - left >= len(longest):
                    longest = s[left:right + 1]
                left -= 1
                right += 1
        return longest