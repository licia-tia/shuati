# -*- coding:utf-8 -*-
class Solution:
    stack = []
    min_stack = []      

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min_stack:
            self.min_stack.append(min(self.min(), node))
        else:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
    def min(self):
        # write code here
        if self.stack:
            return self.min_stack[-1]