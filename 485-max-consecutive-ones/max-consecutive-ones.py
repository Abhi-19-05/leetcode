class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        j = 0

        for m in nums:
            if m == 1:
                i += 1
            else:
                j = max(j, i)
                i = 0

        return max(i, j)