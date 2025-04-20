from collections import Counter

class Solution:
    def numRabbits(self, answers):
        count = Counter(answers)
        total = 0
        for k, v in count.items():
            group_size = k + 1
            groups = (v + k) // group_size
            total += groups * group_size
        return total
