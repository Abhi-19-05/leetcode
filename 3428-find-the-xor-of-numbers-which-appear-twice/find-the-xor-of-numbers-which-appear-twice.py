class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s = set()
        sum = 0

        for i in nums:
            if i in s:
                sum ^= i
            else:
                s.add(i)

        return sum