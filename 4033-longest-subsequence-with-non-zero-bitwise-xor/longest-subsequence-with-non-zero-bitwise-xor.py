class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        k = 0

        for x in nums:
            k ^= x

        if k != 0:
            return len(nums)

        for x in nums:
            if x != 0:
                return len(nums) - 1

        return 0