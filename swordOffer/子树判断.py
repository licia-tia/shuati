# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isTree1HasTree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isTree1HasTree2(pRoot1.left, pRoot2.left) and self.isTree1HasTree2(pRoot1.right, pRoot2.right)


    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 is not None and pRoot2 is not None:
            if pRoot1.val == pRoot2.val:
                result = self.isTree1HasTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result