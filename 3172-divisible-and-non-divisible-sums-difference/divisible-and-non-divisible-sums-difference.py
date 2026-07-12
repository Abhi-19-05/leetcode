class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum=0
        sum1=0
        for i in range(n+1):
            if i%m==0:
                sum=sum+i
            else:
                sum1=sum1+i
        return sum1-sum
