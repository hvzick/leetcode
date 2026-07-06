'''Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''
from collections import deque

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
    def isSameTree(self, p, q) -> bool:
        result = True
        if p is None and q is None:
            return True
        def dfs(p, q):
            nonlocal result
            if p is None and q is None:  # both nodes ended together, so this branch still matches
                return
            elif p is None or q is None: # one tree ended early, so the structure is different
                result = False
                return
            if p.val != q.val:           # node values differ, so the trees are not the same
                result = False
                return
                
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        dfs(p, q)
        return result

p = [1,2,3] 
q = [1,2,3]
a = build_tree(p)
b = build_tree(q)
mySol = Solution()
print(mySol.isSameTree(a, b))