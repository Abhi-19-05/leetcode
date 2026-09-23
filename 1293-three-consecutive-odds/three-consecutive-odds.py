class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        j=1
        k=2
        for i in range(len(arr)-2):
            
            if arr[i]%2!=0 and arr[j]%2!=0 and arr[k]%2!=0:
                return True
            j+=1
            k+=1
        else:
            return False