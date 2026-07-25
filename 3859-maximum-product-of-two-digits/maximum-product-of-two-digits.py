class Solution:
    def maxProduct(self, n: int) -> int:
        s = str(n)
        ans = 0

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                ans = max(ans, int(s[i]) * int(s[j]))

        return ans