class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        x=""
        for i in str(n):
            if int(i)!=0:
                sum=sum+int(i)
                x=x+i
        
        if x == "":
            return 0
        return int(x)*sum
