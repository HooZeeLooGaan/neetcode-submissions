class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0

        curr_max = 0
        max_kadane = float("-inf")

        curr_min = 0
        min_kadane = float("inf")

        for num in nums:
            total_sum += num

            curr_max = max(num, curr_max + num)
            max_kadane = max(max_kadane, curr_max)

            curr_min = min(num, curr_min + num)
            min_kadane = min(min_kadane, curr_min)

        if max_kadane < 0:
            return max_kadane

        return max(max_kadane, total_sum - min_kadane)