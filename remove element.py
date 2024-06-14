'''Given an integer array nums sorted in non-decreasing order,
  remove the duplicates in-place such that each unique element appears only once.
  The relative order of the elements should be kept the same.
  Then return the number of unique elements in nums.'''
class Solution(object):
    def removeElement(self, nums, val):
        # Count the number of occurrences of 'val' in the list 'nums'
        n = nums.count(val)
        # Initialize a counter to keep track of how many elements have been removed
        count = 0
        # Iterate over a copy of the list 'nums' to avoid modifying the list while iterating
        for i in nums[:]:
            # If the current element is equal to 'val'
            if i == val:
                # Remove the element from the list
                nums.remove(i)
                # Increment the counter
                count += 1
            # If the counter reaches the number of occurrences of 'val'
            if count == n:
                # Break out of the loop as all 'val' elements have been removed
                break


# Example usage
sol = Solution()
arr = [0,1,2,2,3,0,4,2]
sol.removeElement(arr, 2)
print(arr)  # Output: [2, 2]





