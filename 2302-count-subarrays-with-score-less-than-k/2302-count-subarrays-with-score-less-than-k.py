class Solution:
    def countSubarrays(self, nums, k):
        left = 0
        total = 0
        ans = 0
        for right in range(len(nums)):
            total += nums[right]
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
