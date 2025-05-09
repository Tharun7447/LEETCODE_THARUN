from itertools import permutations

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        velunexorai = num
        seen = set()
        count = 0

        for p in permutations(velunexorai):
            if p in seen:
                continue
            seen.add(p)
            s = ''.join(p)
            even_sum = sum(int(s[i]) for i in range(0, len(s), 2))
            odd_sum = sum(int(s[i]) for i in range(1, len(s), 2))
            if even_sum == odd_sum:
                count += 1

        return count % MOD
