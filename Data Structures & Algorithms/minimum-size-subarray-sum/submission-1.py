class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        min_len = float("inf")
        summ = 0

        for high in range(len(nums)):
            summ += nums[high]

            while summ >= target:
                min_len = min(min_len, high - low + 1)
                summ -= nums[low]
                low += 1

        return min_len if min_len < float("inf") else 0
