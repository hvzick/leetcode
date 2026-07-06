'''
#TODO Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''

from typing import Optional, List


class Solution:
	class ListNode:
		def __init__(self, val: int = 0, next: 'Optional["Solution.ListNode"]' = None):
			self.val = val
			self.next = next

		def __repr__(self) -> str:
			return f"ListNode({self.val})"

	@staticmethod
	def build_linked_list(vals: List[int]) -> Optional['Solution.ListNode']:
		"""Builds a singly-linked list from a list of integers and returns the head."""
		if not vals:
			return None
		head = Solution.ListNode(vals[0])
		curr = head
		for v in vals[1:]:
			curr.next = Solution.ListNode(v)
			curr = curr.next
		return head

	@staticmethod
	def linked_list_to_list(head: Optional['Solution.ListNode']) -> List[int]:
		"""Converts a linked list back to a Python list of integers."""
		out: List[int] = []
		curr = head
		while curr:
			out.append(curr.val)
			curr = curr.next
		return out

	def deleteDuplicates(self, head: Optional['Solution.ListNode']) -> Optional['Solution.ListNode']:
		# Solution intentionally omitted — helpers only.
		raise NotImplementedError("Solution omitted; only linked list helpers provided.")