class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        st = "".join(str(x) for x in nums)
        sum=0
        sum1=0
        for i in range(len(nums)):
            sum=sum+nums[i]
        for i in range(len(st)):
            sum1=sum1+int(st[i])
        return abs(sum- sum1)
        