class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        low = high = 0
        max_ones = 0

        zero_count = 0
        while high < len(nums):
            if (nums[high] == 0):
                zero_count += 1
            
            while zero_count > k:
                if nums[low] == 0:
                    zero_count -= 1
                low += 1
                    
            max_ones = max(max_ones, high - low + 1)            
            high += 1

        return max_ones