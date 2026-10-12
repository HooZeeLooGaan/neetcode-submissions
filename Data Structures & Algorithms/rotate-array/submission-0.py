class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        for _ in range(k):
            temp = nums[:n]
            nums[0] = nums[n]
            nums[1:] = temp