class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c_o=0
        c_c=0
        for i in s:
            if i=='a' or i=='e'or i=='o'or i=='i'or i=='u':
                c_o+=1
            elif i.isalpha():
                c_c+=1
        if c_c!=0:
            return  c_o//c_c
        else:
            return 0