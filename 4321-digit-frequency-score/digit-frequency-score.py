class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        d={}
        for i in str(n):
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=0
        for key, value in d.items():
            s=s+int(key)*value
        return s
