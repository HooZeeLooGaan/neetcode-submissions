from bisect import bisect_left

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        high = len(nums)
        low = 0
        nums.sort()
        while low <= high:
            mid = (high + low) // 2
            idx = bisect_left(nums, mid)

            if mid == len(nums) - idx:
                return mid

            if mid < len(nums) - idx:
                low = mid + 1

            else:
                high = mid - 1

        return -1

