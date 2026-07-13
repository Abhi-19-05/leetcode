class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=0
        for i in  sentences:
            s=i.split()
            
            if l < len(s):
                l=len(s)
        return l
        