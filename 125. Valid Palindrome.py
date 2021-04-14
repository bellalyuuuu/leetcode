'''
Given a string s, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

# Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers from the start & the end
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# use isalnum(): returns True if all characters in the string are alphanumeric (either alphabets or numbers)

# Time complexity : O(n), in length n of the string.
# We traverse over each character at-most once, until the two pointers meet in the middle,
# or when we break and return early.

# Space complexity :O(1). No extra space required, at all.