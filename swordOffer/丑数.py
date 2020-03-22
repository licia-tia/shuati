# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        tmp = [0]*index
        tmp[0] = 1
        t2, t3, t5 = 0, 0, 0
        for i in range(1, index):
            tmp[i] = min(tmp[t2]*2, tmp[t3]*3,tmp[t5]*5)
            if tmp[i] == tmp[t2]*2:
                t2+=1
            if tmp[i] == tmp[t3]*3:
                t3+=1
            if tmp[i] == tmp[t5]*5:
                t5+=1
        return tmp[index-1]


