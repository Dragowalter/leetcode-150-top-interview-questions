''' You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # pi is the pointer for the last element in the nums1 array
        pi = m - 1
        # pj is the pointer for the last element in nums2 array
        pj = n - 1
        # pk is the pointer for the last element in nums1's merged space
        pk = m + n - 1
        # While there are still elements to compare in nums2
        while pj >= 0:
            # If pi is within bounds and nums1[pi] is greater than nums2[pj]
            if pi >= 0 and nums1[pi] > nums2[pj]:
                # Place nums1[pi] at the current position pointed by pk
                nums1[pk] = nums1[pi]
                # Move pi one position to the left
                pi -= 1
            else:
                # Place nums2[pj] at the current position pointed by pk
                nums1[pk] = nums2[pj]
                # Move pj one position to the left
                pj -= 1
            # Move pk one position to the left
            pk -= 1
# Example usage
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

sol=Solution()
sol.merge(nums1, m, nums2, n)
print(nums1)  # Output should be [1, 2, 2, 3, 5, 6]
