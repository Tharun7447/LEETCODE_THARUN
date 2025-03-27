class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        dominant = max(counter, key=counter.get)
        total_count = counter[dominant]
        left_count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_count += 1
            right_count = total_count - left_count
            
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - (i + 1)):
                return i
        
        return -1
        