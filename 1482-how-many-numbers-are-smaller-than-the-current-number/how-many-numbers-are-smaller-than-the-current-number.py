class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        k=[]
        c=0
        for i in nums:
            for j in nums:
                if i>j:
                    c+=1
            k.append(c)
            c=0
        return k
        
