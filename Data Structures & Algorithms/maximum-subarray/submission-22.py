class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=c=nums[0]
        for r in nums[1:]:
            c=max(r,r+c)
            m=max(m,c)
        return m    
        