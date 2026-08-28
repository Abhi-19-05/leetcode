class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = set(nums)
        n = len(nums)
        count = 0
        k = 0

        for i in s:
            c = nums.count(i)

            if c > n // 2 and count < c:
                count = c
                k = i

        return k
