from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]

        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max  # swap when negative
            
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            
            ans = max(ans, cur_max)
        
        return ans
