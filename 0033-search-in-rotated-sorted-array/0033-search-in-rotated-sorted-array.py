class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        for i in range(n):
            if target == nums[i]:
                return i
        return -1
        