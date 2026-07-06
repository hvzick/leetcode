'''Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # node value
        self.left = left  # left child
        self.right = right  # right child

def build_tree(values):
    if not values or values[0] is None:
        return None  # empty tree

    root = TreeNode(values[0])
    queue = deque([root])  # level-order queue for building children
    i = 1  # index for values array

    while queue and i < len(values):
        node = queue.popleft()  # fill the next available parent

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # attach left child when present
            queue.append(node.left)  # keep the child in the queue for its turn
        i += 1  # move to next value

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # attach right child when present
            queue.append(node.right)  # keep the child in the queue for its turn
        i += 1  # move to next value

    return root  # return constructed tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0                    # base case: empty tree has depth 0
        l = self.maxDepth(root.left)    # recurse left
        r = self.maxDepth(root.right)   # recurse right

        return max(l, r) + 1  # max of both + 1 for current node

mySol = Solution()
root = [3,9,20,None,None,15,7]
tree = build_tree(root)
print(mySol.maxDepth(tree))