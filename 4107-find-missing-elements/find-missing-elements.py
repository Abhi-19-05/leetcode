class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        small=min(nums)
        lar=max(nums)
        k=[]
        for i in range(small,lar+1):
            if i not in s:
                k.append(i)
        return k