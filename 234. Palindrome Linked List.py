'''
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''


# Method 1: Copy into a array list and use two pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #iterative way
        vals = []
        curr = head
        # Step 1: copy linked list into an array
        # Step 2: check if the array is a palindrome (two pointers from both sides to the middle)
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1] #using slice operation [start:end:step],-1 reverse the list

# Time complexity : O(n), where nn is the number of nodes in the Linked List.

# In the first part, we're copying a Linked List into an Array List. \
# Iterating down a Linked List in sequential order is O(n)
# and each of the nn writes to the ArrayList is O(1). Therefore, the overall cost is O(n).

#In the second part, we're using the two pointer technique to
# check whether or not the Array List is a palindrome.
# Each of the nn values in the Array list is accessed once,
# and a total of O(n/2) comparisons are done.
# Therefore, the overall cost is O(n).
# The Python trick (reverse and list comparison as a one liner) is also O(n).
# This gives O(2n)=O(n) because we always drop the constants.

# Space complexity : O(n), where nn is the number of nodes in the Linked List.
#  We are making an Array List and adding n values to it.


# Method 2: fast and slow pointer

#Phase 1: Reverse the first half while finding the middle.
#Phase 2: Compare the reversed first half with the second half.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:  # corner case
            return True
        mid = self.getMid(head)  # find end of first half
        second = self.reverseList(mid.next)  # reverse the second half; get the start of the second half
        first = head  # start of the first half
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    #helper functions below
    def getMid(self, head):  # end of first half
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            # reverse
            temp = curr.next
            curr.next = prev
            # move to the next
            prev = curr
            curr = temp
        return prev

    # Time: O(n), n is the #nodes in the Linked List
    # Finding the middle is O(n), reversing a list in place is O(n), comparing two linked list is O(n)

    # Space: O(1), no extra spaces needed - we are changing each of pointers one-by-one, in-place.

