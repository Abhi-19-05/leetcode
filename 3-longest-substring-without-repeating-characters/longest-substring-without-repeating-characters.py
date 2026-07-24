class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_s=set()
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in char_s:
                char_s.remove(s[l])
                l+=1
            char_s.add(s[i])
            ans=max(ans,i-l+1)
        return ans 

        