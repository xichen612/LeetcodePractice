# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:22:21 2018
@author: chenxi
"""

#给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。

class Solution:
    def multiply(self, A):
        # # write code here
        #思路二：时间复杂度O(n)
        n = len(A)
        B = [1 for i in range(n)]
        for i in range(1,n):
            B[i] = B[i-1] * A[i-1]
        tmp = 1
        for i in range(n-2,-1,-1):
            tmp *= A[i+1]
            B[i] *= tmp
        return B