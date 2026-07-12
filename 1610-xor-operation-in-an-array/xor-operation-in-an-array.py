class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        k=[]
        sum=0
        i=0
        while(i!=n):
            k.append(start+2*i)
            i=i+1
        for i in k:
            sum=sum^i
        return sum


        