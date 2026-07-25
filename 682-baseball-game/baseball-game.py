class Solution:
    def calPoints(self, operations: List[str]) -> int:
      k = []

      for i in operations:
        if i.lstrip('-').isdigit(): 
            k.append(int(i))
        elif i == 'C':
            k.pop()
        elif i == 'D':
            k.append(k[-1] * 2)
        else:
            k.append(k[-1] + k[-2])
         
      return sum(k) 
