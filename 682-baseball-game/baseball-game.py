class Solution:
    def calPoints(self, operations: List[str]) -> int:
        k = []

        for i in operations:
            if i == "C":
                k.pop()

            elif i == "D":
                k.append(2 * k[-1])

            elif i == "+":
                k.append(k[-1] + k[-2])

            else:
                k.append(int(i))

        return sum(k)