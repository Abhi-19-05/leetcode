class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        k=max(candies)
        f=[]
        for i in candies:
            if i+extraCandies >=k:
                f.append(True)
            else:
                f.append(False)
        return f