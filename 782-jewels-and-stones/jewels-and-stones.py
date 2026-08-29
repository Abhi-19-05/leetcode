class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        l=set(jewels)
        c=0
        for i in stones:
            if i in l:
                c+=1
        return c