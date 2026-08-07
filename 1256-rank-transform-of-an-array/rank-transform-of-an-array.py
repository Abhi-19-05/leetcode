
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        d = {}
        ans = []
        rank = 1
        for i in s:
            d[i] = rank
            rank += 1

        
        for i in arr:
            ans.append(d[i])

        return ans