'''Given the root of a binary tree, return the inorder traversal of its nodes' values.'''

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
    def inorderTraversal(self, root) -> list[int]:
        if root is None:
            return []
        left = self.inorderTraversal(root.left)    # visit the left subtree first
        result = left                              # reuse the left traversal result list
        result.append(root.val)                    # then visit the current node
        right = self.inorderTraversal(root.right)  # finally visit the right subtree
        result.extend(right)                       # append the right traversal values
        return result

root = build_tree([1, None, 2, 3])
mySol = Solution()
print(mySol.inorderTraversal(root))