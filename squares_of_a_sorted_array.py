class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [_ for _ in range(len(nums))]
        
        for i in reversed(range(len(nums))):
            # curr = nums[i]
            left = nums[l]
            right = nums[r]
            
            if abs(left) > abs(right):
                res[i] = left * left
                l += 1
            else:
                res[i] = right * right
                r -= 1
        return res
        