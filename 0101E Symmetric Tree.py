'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])  # level-order queue for building children
    i = 1

    while queue and i < len(values):
        node = queue.popleft()  # fill the next available parent

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # attach left child when present
            queue.append(node.left)  # keep the child in the queue for its turn
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # attach right child when present
            queue.append(node.right)  # keep the child in the queue for its turn
        i += 1

    return root

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        result = True
        # assume symmetric until a mismatch is found
        if root is None:
                return True  # empty tree is symmetric
        def dfs(l, r):
            nonlocal result
            if l is None and r is None:
                return  # both sides ended here, this path matches
            elif l is None or r is None:
                result = False  # asymmetric: one side has node, other doesn't
                return 
            if l.val != r.val:
                result = False  # node values differ, not symmetric
                return
            dfs(l.left, r.right)
            dfs(l.right, r.left)

        dfs(root, root)
        return result

mySol = Solution()
root = [1,2,2,3,4,4,3]
tree = build_tree(root)
print(mySol.isSymmetric(tree))