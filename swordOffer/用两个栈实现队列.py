# -*- coding:utf-8 -*-
class Solution:
    stack1 = list()
    stack2 = list()
    def push(self, node):
        # write code here
        while(len(self.stack2)!=0):
            self.stack1.append(self.stack2.pop())
        self.stack1.append(node)
    def pop(self):
        # return xx
        while(len(self.stack1)!=0):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop