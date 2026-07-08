class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        rem = 0
        ans = []

        for bit in nums:
            rem = (rem * 2 + bit) % 5
            ans.append(rem == 0)

        return ans