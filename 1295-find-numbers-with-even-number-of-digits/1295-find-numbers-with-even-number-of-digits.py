class Solution:
    def findNumbers(self, nums):
        return sum(1 for num in nums if len(str(abs(num))) % 2 == 0)
