class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(0, len(nums), 3):
            chunk = nums[i: i+3]
            if chunk[2] - chunk[0] > k:
                return []
            final.append(chunk)
        return final