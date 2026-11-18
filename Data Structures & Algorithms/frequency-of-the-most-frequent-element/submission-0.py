class Solution:

    def _calculate_required_credits(self, nums: list[int]) -> list[int]:
        required_credits = []
        for num in nums:
            required_credits.append(nums[-1] - num)
        return required_credits


    def maxFrequency(self, nums: List[int], k: int) -> int:
        # traverse each element step by step from reverse
        # calculate the diff between subsequent and record max
        # compare subsequent 

        max_freq = 0
        left = right = 0 
        # right = 1
        summ = 0
        nums.sort()

        while right < len(nums):
            right += 1

            while left < right and sum(self._calculate_required_credits(nums[left:right])) > k:
                left += 1
                
            max_freq = max(max_freq, right - left)

        return max_freq