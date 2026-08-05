class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # k=pow(n,1/4)
        # if k**4==n:
        #     return True
        # else:
        #     return False
        if n <= 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4

        return True