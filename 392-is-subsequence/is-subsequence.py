class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for k in t:
            if i<len(s) and s[i]==k:
                i+=1
        return i==len(s)