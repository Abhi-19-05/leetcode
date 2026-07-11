class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        found=0
        
        for i in range(len(hours)):
            if hours[i]>=target:
                found=found+1
                
        else:
            return found