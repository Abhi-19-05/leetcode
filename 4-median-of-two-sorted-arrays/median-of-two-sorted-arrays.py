class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k=nums1+nums2
        k.sort()
        len_=len(k)
        if len_ % 2!=0:
            return (k[len_//2])
        else:
            return ((k[len_// 2] + k[len_ // 2 - 1]) / 2.0)