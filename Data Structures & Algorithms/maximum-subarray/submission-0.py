class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        max_sum = nums[0]

        for num in nums:
            summ = max(summ, 0)
            summ += num
            max_sum = max(max_sum, summ) 

        return max_sum
        