class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums: list[int], low: int, high: int):
        if low < high:
            pivot_idx = self.partition(nums, low, high)

            self.sort(nums, low, pivot_idx - 1)
            self.sort(nums, pivot_idx + 1, high)

    def partition(self, nums: list[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
        