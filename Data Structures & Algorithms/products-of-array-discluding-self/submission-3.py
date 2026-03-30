class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n

        for i in range(n):
            for j in range(n):
                if i != j:
                    product[i] *= nums[j]

        return product