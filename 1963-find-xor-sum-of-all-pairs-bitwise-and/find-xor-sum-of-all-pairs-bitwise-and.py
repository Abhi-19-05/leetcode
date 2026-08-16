class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        x1 = 0
        x2 = 0

        for x in arr1:
            x1 ^= x

        for x in arr2:
            x2 ^= x

        return x1 & x2