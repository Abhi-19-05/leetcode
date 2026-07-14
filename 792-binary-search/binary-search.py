class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid = l + (r - l) // 2
            if nums[int(mid)]==target:
                return mid 
                break
            elif target > nums[int(mid)]:
                l=mid+1
            elif target < nums[int(mid)]:
                r=mid-1
        else:
            return -1