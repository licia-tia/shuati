# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here           
        root = TreeNode(pre[0])
        if len(pre)==1:
            return root

        root_pos = tin.index(pre[0])
        if root_pos!=0:
            root.left = self.reConstructBinaryTree(pre[1:root_pos+1], tin[0:root_pos])
        if len(tin)!=root_pos+1:
            root.right = self.reConstructBinaryTree(pre[root_pos+1:], tin[root_pos+1:])
        return root