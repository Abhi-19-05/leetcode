class Solution:
    def repeatedCharacter(self, s: str) -> str:
        k = set()

        for i in s:
            if i in k:
                return i
            k.add(i)
