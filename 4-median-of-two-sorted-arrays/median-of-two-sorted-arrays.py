class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median=0
        if len(nums1)>0:
            for i in nums2:
                nums1.append(i)
        else:
            nums1=nums2
        if len(nums1)%2 == 1:
            median = sorted(nums1)[math.floor((len(nums1)//2))]
        elif len(nums1)%2 == 0:
            median = (sorted(nums1)[len(nums1)//2] + sorted(nums1)[(len(nums1)//2)-1])/2
        return median
