class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max=0
        nums.sort()
        i=0
        j=1
        while(j<len(nums)):

            c=(nums[i]-1)*(nums[j]-1)
            if c>max:
                max=c
            i+=1
            j+=1
        return max
        