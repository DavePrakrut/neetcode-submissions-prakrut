class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                twosum=n+nums[l]+nums[r]
                if twosum<0:
                    l+=1
                elif twosum>0:
                    r-=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while (l<r and nums[l]==nums[l-1]):
                        l+=1
        return res                       
        