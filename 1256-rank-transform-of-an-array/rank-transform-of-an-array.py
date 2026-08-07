
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        d = {}
        ans = []
        rank = 1
        for num in s:
            d[num] = rank
            rank += 1

        
        for num in arr:
            ans.append(d[num])

        return ans