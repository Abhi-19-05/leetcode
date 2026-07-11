class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for ch in str(num):
            d = int(ch)
            if num % d == 0:
                count += 1
        return count