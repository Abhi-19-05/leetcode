class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a=[]
        b=[]
        for i in nums:
            if i<10:
                a.append(i)
            else:
                b.append(i)
        if sum(a)!=sum(b):
            return True
        else:
            return False
