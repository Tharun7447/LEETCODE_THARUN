from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        alternating = [0] * (2 * n)
        
        for i in range(2 * n - 1):
            alternating[i] = 1 if colors[i % n] != colors[(i + 1) % n] else 0
        
        curr_sum = sum(alternating[:k - 1])
        
        for i in range(n):
            if curr_sum == k - 1:
                count += 1
            curr_sum += alternating[(i + k - 1) % (2 * n - 1)]
            curr_sum -= alternating[i]
        
        return count
