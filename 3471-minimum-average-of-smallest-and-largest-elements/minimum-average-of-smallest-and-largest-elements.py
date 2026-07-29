class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        if len(nums)==0:
            return 0
        s=[]
        avg=0
        nums.sort()
        while len(nums)!=0:
            
            avg=(nums[-1]+nums[0])/2
            s.append(avg)
            nums.remove(nums[-1])
            nums.remove(nums[0])
        return min(s)