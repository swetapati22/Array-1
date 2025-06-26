# Time Complexity :
- O(n), where n is the length of the input array

# Space Complexity :
- O(1), excluding the output array

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Compute prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Compute suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
