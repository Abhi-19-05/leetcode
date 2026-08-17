class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            d=0
            while i:
                d+=1
                i//=10
            if d%2==0:
                c+=1
        return c