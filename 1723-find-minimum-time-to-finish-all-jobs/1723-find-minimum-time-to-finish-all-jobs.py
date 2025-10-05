from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)  # Assign bigger jobs first for better pruning
        workloads = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            if i == len(jobs):
                self.ans = min(self.ans, max(workloads))
                return
            seen = set()
            for w in range(k):
                if workloads[w] in seen:  # avoid duplicate states
                    continue
                if workloads[w] + jobs[i] >= self.ans:
                    continue
                seen.add(workloads[w])
                workloads[w] += jobs[i]
                backtrack(i + 1)
                workloads[w] -= jobs[i]

        backtrack(0)
        return self.ans
