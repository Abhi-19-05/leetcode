class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        i=0
        j=1
        k=2
        while(k<len(arr)):
            if arr[i]%2!=0 and arr[j]%2!=0 and arr[k]%2!=0 :
                return True 
                break
            i+=1
            j+=1
            k+=1
        else:
            return False