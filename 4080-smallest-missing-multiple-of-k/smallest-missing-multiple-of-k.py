class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
       c=1
       while True :
        if c*k not in nums:
            return c*k
        else:
            c+=1
            