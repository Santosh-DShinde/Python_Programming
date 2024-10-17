class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # Dictionary to store number and its index

        # Iterate through the list
        for i, num in enumerate(nums):
            complement = target - num  # Find the complement
            
            # Check if complement is already in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], i]
            
            # If not, add the current number and its index to the dictionary
            num_to_index[num] = i

        # If no solution is found, return an empty list (should not happen based on the problem statement)
        return []

# Test cases
obj = Solution()

# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(obj.twoSum(nums1, target1))  # Output: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
print(obj.twoSum(nums2, target2))  # Output: [1, 2]

# Example 3
nums3 = [3, 3]
target3 = 6
print(obj.twoSum(nums3, target3))  # Output: [0, 1]
                                        