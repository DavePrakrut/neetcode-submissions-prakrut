class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=answer=nums[0]
        for i in nums[1:]:
            cur=max(i,i+cur)
            answer=max(answer,cur)
        return answer    
        