class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l =  0 
        r = 0
        s = nums[0]

        while r < len(nums):
            if s < target:
                r+=1 
                if r < len(nums):
                    s+=nums[r]
            else:
                min_len = min(min_len, r-l+1)
                s-=nums[l]
                l+=1

        return 0 if min_len == float('inf') else min_len
