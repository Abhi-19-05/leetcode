class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        ans = []

        for word in k:
            ans.append(word[::-1])

        return " ".join(ans)