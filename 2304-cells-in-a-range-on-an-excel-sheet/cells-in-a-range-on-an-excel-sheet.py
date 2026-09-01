class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        def col_to_num(col):
            num = 0
            for ch in col:
                num = num * 26 + (ord(ch) - ord('A') + 1)
            return num

        def num_to_col(num):
            col = ""
            while num:
                num -= 1
                col = chr(ord('A') + num % 26) + col
                num //= 26
            return col

        left, right = s.split(':')

        # Separate letters and digits
        i = 0
        while i < len(left) and left[i].isalpha():
            i += 1
        col1 = left[:i]
        row1 = int(left[i:])

        i = 0
        while i < len(right) and right[i].isalpha():
            i += 1
        col2 = right[:i]
        row2 = int(right[i:])

        c1 = col_to_num(col1)
        c2 = col_to_num(col2)

        ans = []

        for c in range(c1, c2 + 1):
            for r in range(row1, row2 + 1):
                ans.append(num_to_col(c) + str(r))

        return ans
