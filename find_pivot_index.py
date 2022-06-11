class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        #total = sum(nums)
        total = 0
        for i in nums:
            total += i
            
        #total = 28
        l_sum = 0
        for i in range(len(nums)):
            curr = nums[i]
            if total - curr - l_sum == l_sum:
                return i
            l_sum += curr
        
        return -1
            