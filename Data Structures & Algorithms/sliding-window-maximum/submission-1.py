class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()  # Stores indices of potential maximums (values in decreasing order)
        
        for i, val in enumerate(nums):
            # 1. Remove elements from the back that are smaller than the current value
            while q and nums[q[-1]] < val:
                q.pop()
                
            q.append(i)
            
            # 2. Remove the front element if it's outside the current window
            if q[0] < i - k + 1:
                q.popleft()
                
            # 3. Append the maximum of the current window to the result
            # (Window is fully formed once i >= k - 1)
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res