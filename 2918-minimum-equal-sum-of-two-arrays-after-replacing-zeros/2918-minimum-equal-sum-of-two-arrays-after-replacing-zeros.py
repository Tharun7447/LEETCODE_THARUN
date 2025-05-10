class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        count0_1, count0_2 = nums1.count(0), nums2.count(0)
        
        if count0_1 == 0 and count0_2 == 0:
            return sum1 if sum1 == sum2 else -1
        
        min_possible_sum1 = sum1 + count0_1 * 1
        max_possible_sum1 = sum1 + count0_1 * int(1e9)
        min_possible_sum2 = sum2 + count0_2 * 1
        max_possible_sum2 = sum2 + count0_2 * int(1e9)
        
        if min_possible_sum1 > max_possible_sum2 or min_possible_sum2 > max_possible_sum1:
            return -1
        
        low = max(min_possible_sum1, min_possible_sum2)
        high = min(max_possible_sum1, max_possible_sum2)
        return low

        