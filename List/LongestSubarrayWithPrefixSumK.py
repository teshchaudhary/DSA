class Solution:
    def longestSubarray(self, nums, target):
        prefix_sum_indices = {}  # Dictionary to store first occurrence of prefix sums
        prefix_sum_indices[0] = -1  # Handle cases where the subarray starts from index 0
        
        current_sum = 0
        max_length = 0  # Stores max length of subarray
        
        for index in range(len(nums)):
            current_sum += nums[index]
            
            # Check if (current_sum - target) has appeared before
            if (current_sum - target) in prefix_sum_indices:
                max_length = max(max_length, index - prefix_sum_indices[current_sum - target])
            
            # Store the first occurrence of current_sum
            if current_sum not in prefix_sum_indices:
                prefix_sum_indices[current_sum] = index
        
        return max_length
