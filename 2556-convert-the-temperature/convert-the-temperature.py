class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k=0
        f=0
        k=celsius + 273.15
        f = celsius * 1.80 + 32.00
        return [k,f]
