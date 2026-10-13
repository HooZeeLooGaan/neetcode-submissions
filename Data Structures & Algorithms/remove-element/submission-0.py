class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while val in nums:
            nums.remove(val)
            i += 1
        
        k = len(nums)
        nums += ['_'] * i
        return k