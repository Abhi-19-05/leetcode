class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if len(nums)<3:
            return "none"
        is_valid = (a + b > c) and (a + c > b) and (b + c > a)
    
        if not is_valid:
            return "none"
        if a==b==c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
