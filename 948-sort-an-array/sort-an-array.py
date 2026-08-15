class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def m_s(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            a = m_s(nums[:mid])
            a1 = m_s(nums[mid:])

            k = []
            i = 0
            j = 0

            while i < len(a) and j < len(a1):
                if a[i] < a1[j]:
                    k.append(a[i])
                    i += 1
                else:
                    k.append(a1[j])
                    j += 1

            while i < len(a):
                k.append(a[i])
                i += 1

            while j < len(a1):
                k.append(a1[j])
                j += 1

            return k

        return m_s(nums)