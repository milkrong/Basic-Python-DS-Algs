# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        for col in range(row):
            if target in array[col]:
                return "true"
                break
        return "false"
