'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


r = TreeNode(5)
l1 = TreeNode(4)
r1 = TreeNode(8)
l2 = TreeNode(11)
r.left = l1
r.right = r1
l1.left = l2
l3 = TreeNode(7)
l2.left = l3
r4 = TreeNode(2)
l2.right = r4

l4 = TreeNode(13)
r2 = TreeNode(4)
r3 = TreeNode(1)

r1.left = l4
r1.right = r2
r2.right = r3

obj = Solution()
print(obj.hasPathSum(r, 22))
