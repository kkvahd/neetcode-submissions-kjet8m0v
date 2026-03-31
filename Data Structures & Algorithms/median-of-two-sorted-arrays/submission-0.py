class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                total.append(nums1[i])
                i += 1
            else:
                total.append(nums2[j])
                j += 1

        while i < len(nums1):
            total.append(nums1[i])
            i += 1
        while j < len(nums2):
            total.append(nums2[j])
            j += 1

        if len(total) % 2 != 0:
            return total[len(total) // 2]
        else:
            m = len(total) // 2
            return (total[m-1] + total[m]) / 2