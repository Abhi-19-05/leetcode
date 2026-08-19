class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        k=[]
        for i in nums:
            if i in k:
                return i
                break
            k.append(i)