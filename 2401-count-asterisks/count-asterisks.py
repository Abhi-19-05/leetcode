class Solution:
    def countAsterisks(self, s: str) -> int:
        y = s.split("|")
     
        a = 0
        for i in y[::2]:
            if "*" in i:
                a+=i.count("*")
        return a