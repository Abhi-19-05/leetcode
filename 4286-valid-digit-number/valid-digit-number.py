class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        k = str(n)

        if int(k[0]) == x:
            return False
        elif str(x) in k:
            return True
        else:
            return False