'''
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                end -= 1
            else:
                i += 1
#del operations takes O(n), so the overall time complexity is O(n^2)

#Two pointers
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

#Time complexity: O(n). Our fast pointer does not visit the same spot twice.
#Space complexity: O(1). All operations are made in-place