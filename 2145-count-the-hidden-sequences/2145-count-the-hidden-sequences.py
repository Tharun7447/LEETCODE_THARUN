class Solution:
    def numberOfArrays(self, differences, lower, upper):
        curr = 0
        min_val = 0
        max_val = 0
        for diff in differences:
            curr += diff
            min_val = min(min_val, curr)
            max_val = max(max_val, curr)
        return max(0, (upper - lower) - (max_val - min_val) + 1)
