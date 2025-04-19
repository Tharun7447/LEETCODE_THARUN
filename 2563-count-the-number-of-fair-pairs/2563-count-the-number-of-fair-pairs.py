from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 1):
            min_j = bisect.bisect_left(nums, lower - nums[i], i + 1)
            max_j = bisect.bisect_right(nums, upper - nums[i], i + 1)
            count += max_j - min_j
        
        return count
