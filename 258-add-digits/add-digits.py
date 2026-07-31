class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0

        while len(str(num)) >= 2:
            ans = sum(int(d) for d in str(num))
            num = ans

        return num
        
            

        