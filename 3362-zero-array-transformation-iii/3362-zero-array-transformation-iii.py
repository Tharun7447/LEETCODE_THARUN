class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key = lambda q: -q[0])
        cur_sum, heap = 0, []
        pref_sum = [0] * (len(nums)+1)
        for i, num in enumerate(nums):
            while queries and i == queries[-1][0]:
                heappush(heap, -queries.pop()[1])
            cur_sum += pref_sum[i]
            num -= cur_sum
            while heap and -heap[0] >= i and num > 0:
                cur_sum += 1
                pref_sum[-heappop(heap)+1] -= 1
                num -= 1
            if num > 0:
                return -1
        return len(heap)