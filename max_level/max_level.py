'''
Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, 
the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values 
of nodes at level x is maximal.
Example:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

'''
from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels = defaultdict(int)
        def sum_vals(root, depth):
            if root:
                levels[depth] += root.val
                sum_vals(root.left,  depth+1)
                sum_vals(root.right, depth+1)
			
        sum_vals(root, 1)
        return max(levels, key=levels.get)


###############Version 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    def maxLevelSumVersion2(self, root) -> int:
        
        if not root.left and not root.right:
            return 1
        
        
        level = [root]
        level_num = 1
        ans_level = 0
        max_val = float('-inf')
        
        while level:
            temp = [node.val for node in level]
            total = sum(temp)
            
            if total > max_val:
                max_val = total
                ans_level = level_num
            
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            
            level_num += 1
        
        return ans_level
