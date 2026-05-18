class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ts={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in ts:
                return[ts[diff],i]
            ts[n]=i
        return[]        
        