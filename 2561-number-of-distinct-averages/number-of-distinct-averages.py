class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        s=set()
        avg=0
        nums.sort()
        while len(nums)!=0:
            
            avg=(nums[-1]+nums[0])/2
            s.add(avg)
            nums.remove(nums[-1])
            nums.remove(nums[0])
        return len(s)

        
