# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        if len(array)==1:
            return array
        oddCnt = 0
        for i in array:
            if i%2==0:
                oddCnt+=1
        ans = [0]*len(array)
        cntEven = 0
        cntOdd = 0
        for i in array:
            if i%2!=0:
                ans[cntEven] = i
                cntEven+=1
            else:
                ans[cntOdd+oddCnt+1] = i
                cntOdd+=1
        return ans
