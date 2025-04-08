class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) != len(set(nums)):
            nums = nums[3:]
            ops += 1
        return ops