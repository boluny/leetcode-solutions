# -*- coding: utf-8 -*-

#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.74%)
# Likes:    1546
# Dislikes: 41
# Total Accepted:    392.1K
# Total Submissions: 800.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from helper.tree import TreeNode
from helper.tree import stringToTreeNode
from helper.tree import treeNodeToString

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        ret = []
        one_level = []
        current_level_nodes = [root]
        next_level_nodes = []
        
        # We can even validation utilizing node count
        # level = 0
        # curernt_level_threshold = level ** 2
        # next_level_threshold = curernt_level_threshold * 2
        while current_level_nodes:
            # we handle the current node 
            node = current_level_nodes.pop(0)
            if node.left:
                next_level_nodes.append(node.left)

            if node.right:
                next_level_nodes.append(node.right)

            one_level.append(node.val)

            # Check if it's the last node in current level
            # 1. submit current level order
            # 2. escalate next level nodes to current and reset next level variable
            if not current_level_nodes:
                ret.append(one_level)
                one_level = []
                current_level_nodes = next_level_nodes
                next_level_nodes = []

        return ret

def test_solution():
    root = stringToTreeNode('[3,9,20,null,null,15,7]')
    ss = Solution()
    result = ss.levelOrder(root)
    assert [[3],[9,20],[15,7]] == result
