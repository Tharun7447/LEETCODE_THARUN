from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Pair engineers as (efficiency, speed) and sort by efficiency desc
        engineers = sorted(zip(efficiency, speed), reverse=True)
        
        speed_heap = []  # min-heap for speeds
        speed_sum = 0
        max_perf = 0
        
        for eff, spd in engineers:
            # If we already have k engineers, remove the one with smallest speed
            if len(speed_heap) == k:
                speed_sum -= heapq.heappop(speed_heap)
            
            # Add this engineer
            heapq.heappush(speed_heap, spd)
            speed_sum += spd
            
            # Calculate performance with current engineer's efficiency as minimum
            max_perf = max(max_perf, speed_sum * eff)
        
        return max_perf % MOD

        