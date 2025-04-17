class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)
        cnt = 0
        for lst in idx_map.values():
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    if (lst[i] * lst[j]) % k == 0:
                        cnt += 1
        return cnt

        