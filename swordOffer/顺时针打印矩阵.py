# -*- coding:utf-8 -*-

# pop大法
# https://blog.csdn.net/qq_20141867/article/details/80902980
# 大力旋转矩阵
# https://blog.csdn.net/slibra_L/article/details/78185653
class Solution:
    def printMatrix(self, matrix):
        out = []
        while matrix:
            # 上边界即为数组的第一个子数组
            out += matrix.pop(0)
            # 如果这里仅判断if matrix，那么对于测试数组例[[1],[2],[3]]，循环后变成了[[],[]]，matrix不为空
            if matrix and matrix[0]:
                # 右边界即为数组每一项的最后一个元素
                for row in matrix:
                    out.append(row.pop())
            # 下边界即为数组最后一个子数组的逆序排列
            if matrix:
                out += matrix.pop()[::-1]
            if matrix and matrix[0]:
                # 左边界即为数组从尾到头的每一项子数组的第一个元素
                for row in matrix[::-1]:
                    out.append(row.pop(0))
        return out
