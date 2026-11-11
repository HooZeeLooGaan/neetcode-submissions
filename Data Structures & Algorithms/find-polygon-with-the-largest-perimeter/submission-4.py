class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        final = 0
        res = -1
        nums.sort()
        for num in nums:
            if final > num:
                res = final + num
            final += num

        return res
