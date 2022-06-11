class Solution:
    def twoSum(self, nums, target):  
        hashmap = {}
        for i in range(len(nums)):
            curr = nums[i]
            res = target - curr
            if res in hashmap:
                return [i, hashmap[res]]
            hashmap[curr] = i      
        return -1