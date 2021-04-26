'''
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

#Use Sets
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return [x for x in set1 if x in set2]
    # or
        #return list(set1 & set2)
#Time: O(n+m), where n and m are arrays' lengths.
#Space: O(m+n) in the worst case when all elements in the arrays are different.

#use dict / hashmap

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d  = {}
        res = []
        for num in nums1:
            d[num]=1
        for num in nums2:
            if num in d and d[num]>0:
                res.append(num)
                d[num]=0 #avoid duplicate
        return res
#O(m + n) Time and O(n) Space where n = len(nums1), m = len(nums2)