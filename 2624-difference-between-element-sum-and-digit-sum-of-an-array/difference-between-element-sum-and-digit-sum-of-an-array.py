class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        st = "".join(str(x) for x in nums)
        sum_=sum(nums)
        sum1=0
    
        for i in range(len(st)):
            sum1=sum1+int(st[i])
        return abs(sum_- sum1)
        