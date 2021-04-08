'''
1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i, num in enumerate(nums):
            n = target-num
            if n not in dic:
                dic[num]=i
            else:
                return [dic[n], i]

# Time Complexity: O(n). We traverse the list containing nn elements only once.
# Each look up in the table costs only O(1) time.

# Space complexity : O(n).
# The extra space required depends on the number of items stored in the hash table,
# which stores exactly n elements.