'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    # O(n ^ 2)
    def twoSum(self, nums, target):
        i = 0
        ans1 = -1
        ans2 = -1
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                val = target - nums[i]
                if nums[j] == val:
                    ans1 = i
                    ans2 = j
                    break
                j += 1
            i += 1
        return ([ans1, ans2])
    
    # O(1)
    def twoSumLin(self, nums, target):
        
        # the dictionary is empty at first
        log_dict = {}
        for i in range(len(nums)):
            
            # if the element is a key in the dict, this means we have previously already found a value that maches with this element 
            # therefore return this the matching value's index and the element's index
            if nums[i] in log_dict:
                return [log_dict[nums[i]], i]
            
            # if the element is not present in the dict, store the elements index as value and the number that it would match with as the key 
            else:
                log_dict[target - nums[i]] = i
                